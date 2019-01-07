#!/usr/bin/env python
import boto3
import json

class aws_vpcd():
        def vpc(self):
	    self.ec2=boto3.client("ec2")
	    self.v_vpc_info=self.ec2.describe_vpcs()
	    self.v_igw_info=self.ec2.describe_internet_gateways()
	    for v_vpc in range(len(self.v_vpc_info['Vpcs'])):
		vpcid=self.v_vpc_info['Vpcs'][v_vpc]['VpcId']
		vpcidtag=self.v_vpc_info['Vpcs'][v_vpc]['CidrBlock']
		igwid=self.v_igw_info['InternetGateways'][v_vpc]['InternetGatewayId']
		igwtag=self.v_igw_info['InternetGateways'][v_vpc]['Tags']
 		print vpcid
 		print vpcidtag
		print igwid
		print igwtag
	
	def aws_vpcfile(self):
	    fp=open("network.json")
	    self.v_data=json.load(fp)
	    cust_cidr=self.v_data["aws_vpc"]["vpc"]["vpccidr"]
	    print( "{}.is customer cidr required to be deleted".format(cust_cidr))
            fp.close()
  
	def aws_igwsearch(self):
	    fp=open("network.json")
            self.v_data=json.load(fp)
	    cust_igwtag=self.v_data["aws_vpc"]["igw"]["Igwname"]
	    print cust_igwtag

s=aws_vpcd()
s.vpc()
s.aws_vpcfile()
#s.aws_igwsearch()
