import boto3

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
        # else:
        #     return instances.id


def lambda_handler(event, context):
    global ec2r

    # Iterate over regions
    for region in regionslist:
        print("Region %s " % region['RegionName'])
        print("===========================================\n")
        reg = region['RegionName']

        # Connect to region
        ec2r = boto3.resource('ec2', region_name=reg)

        # Get a list of all instances
        running_instances = [i for i in ec2r.instances.filter(Filters=
                                                              [{'Name': 'instance-state-name', 'Values': ['running']}])]

        # Get instances with filter of running + with tag `Name`
        skip_instances = [i for i in ec2r.instances.filter(Filters=
                                                           [{'Name': 'instance-state-name', 'Values': ['running']},
                                                            {'Name': 'tag:skip_shutdown', 'Values': ['']}])]

        # Get spot instances
        spot_instances = [i for i in ec2r.instances.filter(Filters=
                                                           [{'Name': 'instance-state-name', 'Values': ['running']},
                                                            {'Name': 'instance-lifecycle', 'Values': ['spot']}])]
        # Get the amount of the running instances

        if len(running_instances) > 0:
            print("The amount of running instances in this region is: ", len(running_instances), "\n")

            # Get the amount instances with tag skip_shutdown
            if len(skip_instances) > 0:
                print("The amount of running instances with tag skip_shutdown is: ", len(skip_instances), "\n")

            else:
                print("No running instances with tag skip_shutdown in this region")

        # Get The amount of spot instances
        elif len(spot_instances) > 0:
            print("The amount of running Spot instances is: ", len(spot_instances), "\n")

        else:
            print("No running instances in this region")

        # Get the names of spot instances
        if len(spot_instances) > 0:
            for spot_instance in spot_instances:
                if get_tags(spot_instance):
                    print("The spot instances name will not stop: ", get_tags(spot_instance),
                          " spot instance id: ", spot_instance.id, "\n")

                elif not get_tags(spot_instance):
                    print("The spot instances without name that will not stop", spot_instance.id)

        # Filter from all instances the instance that are not in the filtered list
        instances_to_stop = [to_stop for to_stop in running_instances
                             if to_stop.id not in [instance.id for instance in skip_instances]
                             and to_stop.id not in [instance.id for instance in spot_instances]]

        # Run over your `instances_to_stop` list and stop each one of them
        try:
            for instance in instances_to_stop:
                # instance.stop()
                # print(instance.id)
                if get_tags(instance):
                    print("The instances name to stop: ", get_tags(instance),
                          " instance id: ", instance.id, "\n")

                elif not get_tags(instance):
                    print("The instances without name that will stop", instance.id)

        except Exception as e:
            print("You cant stop spot instances")
            print("Error: ", e)
            continue

        print("===========================================\n")
    print('Done.')


# This is for local testing don't remove
if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)
