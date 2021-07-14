import boto3

# Define client connection
ec2c = boto3.client('ec2')

# Get list of regions
regionList = ec2c.describe_regions().get('Regions', [])

# KMS key description
key_description = '<KeyDescription>>'


def delete_kms_keys(desc, reg):
    kms_client = boto3.client('kms', region_name=reg)
    match_state = "Enabled"
    marker = None

    while True:
        paginator = kms_client.get_paginator('list_keys')
        response_iterator = paginator.paginate(PaginationConfig={'PageSize': 100, 'StartingToken': marker})

        for cmk in response_iterator:
            keys = cmk['Keys']
            marker = cmk['Truncated']
            while marker is True:
                for key in keys:
                    key_info = kms_client.describe_key(KeyId=key['KeyArn'])
                    key_id = key_info['KeyMetadata']['KeyId']
                    key_desc = key_info['KeyMetadata']['Description']
                    key_state = (key_info['KeyMetadata']['KeyState'])
                    if match_state == key_state and key_desc == key_description:
                        print("Deleting key: ", key_id)
                        kms_client.schedule_key_deletion(KeyId=key_id, PendingWindowInDays=7)
                        break
                break
            continue
        return print("All keys were checked and no keys to delete!\n")


def lambda_handler(event, context):
    for region in regionList:
        print("Region %s " % region['RegionName'])
        print("===========================================\n")
        reg = region['RegionName']

        delete_kms_keys(key_description, reg)
        print("Moving to next region\n")


if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)
