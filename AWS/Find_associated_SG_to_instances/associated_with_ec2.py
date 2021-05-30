import boto3
import csv

# Define client connection
ec2c = boto3.client('ec2')

# Define ressources connection
ec2r = boto3.resource('ec2')

# Get list of regions
regionslist = ec2c.describe_regions().get('Regions', [])


# Function to get tags from instances
def get_tags(instances):
    for tag in instances.tags:
        if tag['Key'] == 'Name':
            instances_tags = tag['Value']
            return instances_tags


def lambda_handler(event, context):
    global ec2r
    result = []

    # Iterate over regions
    for region in regionslist:
        print("Region %s " % region['RegionName'])
        print("===========================================\n")
        reg = region['RegionName']

        result.append({
            'Region': region['RegionName']
        })

        # Connect to region
        ec2r = boto3.resource('ec2', region_name=reg)

        ec2c = boto3.client('ec2', region_name=reg)

        response = ec2c.describe_instances()

        try:
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    print("\nInstance: " + instance['InstanceId'], "  Instance state: ", instance['State']['Name'])
                    for securityGroup in instance['SecurityGroups']:
                        result.append({
                            'InstanceId': instance['InstanceId'],
                            'InstanceType': instance['InstanceType'],
                            'InstanceState': instance['State']['Name'],
                            'GroupId': securityGroup['GroupId'],
                            'GroupName': securityGroup['GroupName']
                        })

                        print("SG ID: {}, Name: {}".format(securityGroup['GroupId'], securityGroup['GroupName']))

        except Exception as E:
            print(region, E)
            continue
        print("===========================================\n")
    print('Done.')

    # 'region','ImageId', 'InstanceType', 'PublicIp', 'PrivateIp'
    header = ['Region', 'InstanceId', 'InstanceType', 'InstanceState', 'GroupId', 'GroupName']
    with open('ec2-details.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(result)


# This is for local testing don't remove
if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)
