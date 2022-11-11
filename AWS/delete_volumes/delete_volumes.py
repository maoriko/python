import locale

import boto3
from lazyme.string import color_print

import operator

# Define client connection
ec2_client = boto3.client('ec2')

# Get list of regions
regionList = ec2_client.describe_regions().get('Regions', [])
in_use_volumes = []
available_volumes = []
vol_in_use = {"Name": "status", "Values": ["in-use"]}
vol_available = {"Name": "status", "Values": ["available"]}
initial = 0


def get_volume_info(current_region):
    ec2 = boto3.resource('ec2', region_name=current_region)
    total = 0

    for vol in ec2.volumes.filter(Filters=[vol_in_use]):
        volume = vol.id
        volume_id = ec2.Volume(vol.id)
        volume_size = volume_id.size
        volume_state = volume_id.state
        volume_type = volume_id.volume_type
        volume_encryption = volume_id.encrypted
        in_use_volumes.append(volume_size)

        if len(in_use_volumes) < 0:
            print(f'No volumes founded {current_region}')
            break
        else:
            print(f'Volume_id {volume} Volume_type {volume_type} ({volume_size} GiB) Volume encrypted {volume_encryption} -> {volume_state}')

    for num in in_use_volumes:
        total += num

    print(f'\nTotal size of volumes for region {current_region} is {total}GB')
    in_use_volumes.clear()


def delete_unused_volumes(current_region):
    ec2 = boto3.resource('ec2', region_name=current_region)

    for vol in ec2.volumes.filter(Filters=[vol_available]):
        volume = vol.id
        volume_id = ec2.Volume(vol.id)
        volume_size = volume_id.size
        volume_state = volume_id.state
        volume_type = volume_id.volume_type
        volume_encryption = volume_id.encrypted

        available_volumes.append(volume)

        if len(available_volumes) < 0:
            print(f'No volumes founded {current_region}')
            break
        else:
            print(f'Volume_id {volume} Volume_type {volume_type} ({volume_size} GiB) Volume encrypted {volume_encryption} -> {volume_state}')
            # volume.delete()


# get_volume_info("us-east-1")

for region in regionList:
    print("Region %s " % region['RegionName'])
    print("===========================================\n")
    reg = region['RegionName']
    # Call EC2 deletion process
    get_volume_info(reg)
    print("===========================================\n")
    continue
print('Done.')
