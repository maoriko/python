import boto3
import csv


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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

        # Connect to region
        ec2r = boto3.resource('ec2', region_name=reg)

        ec2c = boto3.client('ec2', region_name=reg)

        response = ec2c.describe_instances()

        try:
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    print(Color.BOLD + "\nInstanceID: " + Color.END + Color.BLUE + instance['InstanceId'] + Color.END +
                          Color.BOLD + "  Instance state: " + Color.END + Color.GREEN + instance['State']['Name'] + Color.END)
                    for securityGroup in instance['SecurityGroups']:
                        result.append({
                            'Region': region['RegionName'],
                            'InstanceId': instance['InstanceId'],
                            'InstanceType': instance['InstanceType'],
                            'InstanceState': instance['State']['Name'],
                            'SGroupId': securityGroup['GroupId'],
                            'SGroupName': securityGroup['GroupName']
                        })
                        print(Color.BOLD + "SecurityGroup ID: " + Color.END + Color.RED + securityGroup['GroupId'] + Color.END +
                              Color.BOLD + "  SecurityGroup Name: " + Color.END + Color.PURPLE + securityGroup['GroupName'] + Color.END)

        except Exception as E:
            print(region, E)
            continue

        print("===========================================\n")
    print('Done.')

    header = ['Region', 'InstanceId', 'InstanceType', 'InstanceState', 'SGroupId', 'SGroupName']
    with open('ec2-details.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(result)


# This is for local testing don't remove
if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)