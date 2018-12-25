#!/usr/bin/env python
import boto3
import json
import logging
import time
logging.basicConfig(level="INFO",format='%(asctime)s:%(message)s')

class aws_vpc:
        def __init__(self):
            self.ec2=boto3.resource("ec2")
            fp=open("network.json")
	    try:
       	        self.v_data=json.load(fp)
		logging.info("network.json file is in good state")
	    except ValueError as v_error:
		logging.error("{} is the error in network.json file".format(v_error))
            fp.close()
                
        def vpc_create(self):
            v_vpcname=self.v_data["aws_vpc"]["vpc"]["vpcname"]
            v_vpccidr=self.v_data["aws_vpc"]["vpc"]["vpccidr"]
            logging.info("checking if vpc already exists")
	    vpc_obj=boto3.client("ec2")
            v_vpc_info=vpc_obj.describe_vpcs()
	    v_flag=False
	    for v_vpcn in range(len(v_vpc_info["Vpcs"])):
		cidr= v_vpc_info["Vpcs"][v_vpcn]["CidrBlock"]
		if cidr == v_vpccidr:
		   v_flag=True
            if v_flag == True:
		logging.error("{} address space overlapping ...".format(v_vpccidr))
		time.sleep(5)
		exit(123)
            self.v_vpc=self.ec2.create_vpc(CidrBlock=v_vpccidr)
            self.v_vpc.create_tags(Tags=[{"Key":"Name","Value":v_vpcname}])
            
        def subnet_create(self):
	    for v_sub in self.v_data["aws_vpc"]["subnet"]:
		v_subnetname=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_name"]
		v_subnetcidr=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_cidr"]
		subnet = self.ec2.create_subnet(CidrBlock=v_subnetcidr, VpcId=self.v_vpc.id)
		subnet.create_tags(Tags=[{"Key":"Name","Value":v_subnetname}])
	def igw_create(self):
	   	v_igwname=self.v_data["aws_vpc"]["igw"]["Igwname"]
        	logging.info("create igw ..")
		self.v_igw=self.ec2.create_internet_gateway()
		self.v_igw.create_tags(Tags=[{"Key":"Name","Value":v_igwname}])
		logging.info("igw created successfully")
s=aws_vpc()
s.vpc_create()
s.subnet_create()
s.igw_create()
