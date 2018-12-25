#!/usr/bin/env python
import sys
import boto3
vpcid=raw_input('vpcid: ' )
ec2 = boto3.client('ec2')
response = ec2.delete_vpc(VpcId=vpcid)
print response
