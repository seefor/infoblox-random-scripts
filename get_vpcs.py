import boto3
import json

ec2 = boto3.resource('ec2', aws_access_key_id='AKIAQCXDINN5HJASERV7',
                     aws_secret_access_key='OD+asdasdasdasd',
                     region_name='us-east-2')

client = boto3.client('ec2', aws_access_key_id='AKIAQCXDINN5HJASERV7',
                     aws_secret_access_key='OD+asdasdasdasd',
                     region_name='us-east-2')

filters = [{'Name':'tag:Name', 'Values':['*']}]

vpcs = list(ec2.vpcs.filter(Filters=filters))

print(vpcs)

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[
            vpc.id,
        ]
    )
    #print(json.dumps(response, sort_keys=True, indent=4))
    for vpc in response["Vpcs"]:
        vpc_id = vpc["VpcId"]
        vpc_cidr=vpc["CidrBlock"]
        vpc_isdefault = vpc["IsDefault"]
        vpc_ownerid = vpc["OwnerId"]
        vpc_state = vpc["State"]
        vpc_name = vpc["Tags"][0]["Value"]
        print("Updating AWS Account "+ vpc_ownerid + " in the VPC Tracker")
        print(vpc_id)
        print(vpc_cidr)
        print(vpc_isdefault)
        print(vpc_state)
        print(vpc_name)
