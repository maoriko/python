import boto3

final_eip = {}
eips = [
    "XXX.XXX.XXX.XXX"
]

print("The amount of IP's to scan is:", len(eips))
ec2_client = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2_client.describe_regions()
region_list = response['Regions']


def ip_address_finder(region):
    counter = 0
    client = boto3.client('ec2', region_name=region["RegionName"])
    try:
        addresses_dict = client.describe_addresses()

        for eip_dict in addresses_dict['Addresses']:
            ip = eip_dict['PublicIp']
            if ip in eips:
                instance_id = ""
                if eip_dict.get('InstanceId'):
                    instance_id = eip_dict.get('InstanceId')
                counter += 1
                print(f"ip - {ip} instance id = {instance_id}")

    except:
        pass


for region in region_list:
    print("Region %s " % region['RegionName'])
    print("===========================================\n")
    reg = region['RegionName']

    ip_address_finder(region)

    print("===========================================\n")
print('Done.')
