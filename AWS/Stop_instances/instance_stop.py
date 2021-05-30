import boto3

# Define client connection
ec2c = boto3.client('ec2')

# Define ressources connection
ec2r = boto3.resource('ec2')

# Get list of regions
regionslist = ec2c.describe_regions().get('Regions', [])


def lambda_handler(event, context):
    global ec2r

    # Iterate over regions
    for region in regionslist:
        print("Region %s " % region['RegionName'])
        reg = region['RegionName']

        # Connect to region
        ec2r = boto3.resource('ec2', region_name=reg)

        # Get a list of all instances
        all_running_instances = [i for i in
                                 ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]

        # Get instances with filter of running + with tag `Name`
        instances = [i for i in ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
                                                               {'Name': 'tag:skip_shutdown', 'Values': ['']}])]

        # Get the amount of the running instances
        if len(all_running_instances) > 0:
            print("The amount of running instances in this region is: ", len(all_running_instances))
        else:
            print("No running instances in this region")

        # Get the amount instances with tag skip_shutdown
        if len(instances) > 0:
            print("The amount of running instances with tag skip_shutdown is: ", len(instances))

        # Filter from all instances the instance that are not in the filtered list
        instances_to_stop = [to_stop for to_stop in all_running_instances if to_stop.id not in [i.id for i in instances]]

        # Run over your `instances_to_stop` list and stop each one of them
        for instance in instances_to_stop:
            for tag in instance.tags:
                if tag['Key'] == 'Name':
                    tag_names = tag['Value']
                    print("The instances names going to be stopped: ", tag_names, " instance id: ", instance.id)
                    break
                else:
                    print("The instances with no name going to be stopped: ", instance.id)
                    break
            instance.stop()

        print("=================================\n")

    print('Done.')


# This is for local testing don't remove
# if __name__ == "__main__":
#     event = []
#     context = []
#     lambda_handler(event, context)
