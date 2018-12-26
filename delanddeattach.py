#!//usr/bin/env python
import boto3
import time
import sys
from botocore.exceptions import ClientError

class igwops:
	
	def __init__(self):
	#detach_internet_gateway
		self.ec2=boto3.client("ec2")
		igw=raw_input('igwid: ' )
		vpcid=raw_input('vpcid: ' )
		
		try:

			response = self.ec2.detach_internet_gateway(InternetGatewayId=igw, VpcId=vpcid)
			print ("igw deattached successfully")
		except ClientError as igw_error:
			print ("igw is deattached already as {}".format(igw_error))
			response1 = self.ec2.delete_internet_gateway(InternetGatewayId=igw)
			print ("igw deleted successfully with id:{}".format(igw))

s=igwops()
