import ssl, socket
import datetime, requests, boto3, os, json, sys

access_key = os.environ.get("ACCESS_KEY_ID")
secret_key = os.environ.get("SECRET_ACCESS_KEY")
r53_zone_id = os.environ.get("HOSTED_ZONE_ID")
exp_limit = 25


def get_route53_records(zone_id):
    client = boto3.client('route53',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key
                          )

    response = client.list_resource_record_sets(
        HostedZoneId=zone_id
    )

    subdomains = []
    paginator = client.get_paginator('list_resource_record_sets')

    try:
        zone_records = paginator.paginate(HostedZoneId=zone_id)
        for record_set in zone_records:
            for record in record_set['ResourceRecordSets']:
                if record['Type'] in ['A']:
                    subdomains.append(record['Name'])

        print(f"[*] Total Number of A records in hosted zone: {len(subdomains)}")
    except Exception as error:
        print(error)

    return subdomains


def sort_subdomains(subdomains):
    subdomains_list = []
    sorted_list = []
    [subdomains_list.append(subdomain) for subdomain in subdomains if subdomain not in subdomains_list]

    for subdomain in subdomains_list:
        subdomain = subdomain[:-1]
        if "mq" in subdomain:
            sorted_list.append({'hostname': subdomain, 'port': 5671})
        elif "zt.wmt" in subdomain:
            sorted_list.append({'hostname': subdomain, 'port': 9300})
        elif "zt" in subdomain:
            sorted_list.append({'hostname': subdomain, 'port': 9900})
        elif "splunk" in subdomain:
            sorted_list.append({'hostname': subdomain, 'port': 9443})
        elif "restore" in subdomain or "log." in subdomain:
            pass
        else:
            sorted_list.append({'hostname': subdomain, 'port': 443})

    print(f"[*] Total Number of sorted records for check in hosted zone: {len(sorted_list)}")

    return sorted_list


def get_certificate(hostname, port):
    context = ssl.create_default_context()
    try:
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname) as sock:
            sock.settimeout(3.0)
            try:
                sock.connect((hostname, port))
                certificate = sock.getpeercert()
                return certificate
            except Exception as e:
                print(e, hostname, port)

    except Exception as e:
        print(e, hostname, port)


def get_expiration_date(exp_date):
    ssl_dateformat = r'%b  %d %H:%M:%S %Y %Z'
    now = datetime.datetime.now()
    days_left = datetime.datetime.strptime(exp_date, ssl_dateformat)
    delta = days_left - now
    return delta


def send_slack_notification(notification):
    url = os.environ.get("SLACK_TOKEN")
    message = notification
    title = "SSL Certificate Expiration Alert"

    slack_data = {
        "attachments": [
            {
                "color": "#bd3232",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }

    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


def lambda_handler(event, context):
    print("[*] Starting subdomains certificates check...\n")
    route53_records = get_route53_records(r53_zone_id)
    subdomains = sort_subdomains(route53_records)

    for subdomain in subdomains:
        cert = get_certificate(subdomain['hostname'], subdomain['port'])
        if cert:
            exp_days = get_expiration_date(cert['notAfter'])
            if exp_days.days < exp_limit:
                notification = f"WARNING: {subdomain['hostname']} certificate is about to expire in: {exp_days.days} days!"
                print(notification)
                send_slack_notification(notification)
            else:
                print(f"[*] {subdomain['hostname']} certificate will be expired in: {exp_days.days} days")

# This is for local testing don't remove
# if __name__ == "__main__":
#     event = []
#     context = []
#     lambda_handler(event, context)
