#!/usr/bin/env	python
#d['Reservations'][0]['Instances'][0]['PrivateIpAddress']
import boto3
import logging
logging.basicConfig(level="INFO",format='%(asctime)s:%(message)s')
class ec2_list:
	def __init__(self):
		self.ec2=boto3.client("ec2")
		self.d=self.ec2.describe_instances()
	def extract_data(self):
		for i in range(len(self.d['Reservations'])):
			print self.d['Reservations'][i]['Instances'][0]['PrivateIpAddress']
			print self.d['Reservations'][i]['Instances'][0]['Monitoring']['State']
			print self.d['Reservations'][i]['Instances'][0]['ImageId']

d1=ec2_list()
d1.extract_data()
			
