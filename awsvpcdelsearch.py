#!/usr/bin/env python
import boto3
import json

class aws_vpcd():
        def vpc(self):
	    self.ec2=boto3.client("ec2")
	    self.v_vpc_info=self.ec2.describe_vpcs()
	    for v_vpc in range(len(self.v_vpc_info['Vpcs'])):
		vpcid=self.v_vpc_info['Vpcs'][v_vpc]['VpcId']
		vpcidtag=self.v_vpc_info['Vpcs'][v_vpc]['CidrBlock']
 		print vpcid
 		print vpcidtag
	
	def aws_vpcfile(self):
	    fp=open("network.json")
	    self.v_data=json.load(fp)
	    cust_cidr=self.v_data["aws_vpc"]["vpc"]["vpccidr"]
	    print( "{}.is customer cidr required to be deleted".format(cust_cidr))
            fp.close()
  
s=aws_vpcd()
s.vpc()
s.aws_vpcfile()
