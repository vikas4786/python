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
	    time.sleep(2)
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
            print ( "vpc created successfully with id {}".format(self.v_vpc))
            
	def subnet_create(self):
	    self.subnet_list=[]
            for v_sub in self.v_data["aws_vpc"]["subnet"]:
               	v_subnetname=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_name"]
            	v_subnetcidr=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_cidr"]
                self.subnet = self.ec2.create_subnet(CidrBlock=v_subnetcidr, VpcId=self.v_vpc.id)
                print ( "subnet created successfully with id {}".format(self.subnet.id))
                self.subnet.create_tags(Tags=[{"Key":"Name","Value":v_subnetname}])
		self.subnet_list.append(self.subnet.id)
	        print self.subnet_list
	def igw_create(self):
	   	v_igwname=self.v_data["aws_vpc"]["igw"]["Igwname"]
        	logging.info("create igw ..")
		self.v_igw=self.ec2.create_internet_gateway()
		self.v_igw.create_tags(Tags=[{"Key":"Name","Value":v_igwname}])
		logging.info("igw created successfully")
	def attach_igw(self):
		logging.info("attaching igw with vpc..")
		self.v_vpc.attach_internet_gateway(InternetGatewayId=self.v_igw.id)
		time.sleep(5)
		logging.info("igw attach to vpc successfully..")
	def route_create(self):
		self.route_list=[]
		for v_router in self.v_data["aws_vpc"]["router"].keys():
			v_rname=self.v_data["aws_vpc"]["router"][v_router]["router_name"]
			logging.info("creating route table..")
			self.route_table=self.ec2.create_route_table(DryRun=False,VpcId=self.v_vpc.id)
			self.route_table.create_tags(Tags=[{'Key':'Name','Value':v_rname}])
			self.route_list.append(self.route_table)
			print self.route_list
			logging.info("{} route table created successfully".format(v_rname))
		 	s.associate_route()
	def create_eip(self):
	        self.Ec2_Eip=boto3.client('ec2')
        	self.V_Eip=self.Ec2_Eip.allocate_address(Domain=self.v_vpc.id)
		print("elastic ip created sucessfully with id{}".format(self,V_Eip.id))
		time.sleep(3)
	def create_natgw(self):
        #nat_gw = client.create_nat_gateway(SubnetId=subnet1.id,AllocationId=eip.id)
        	self.natgw=self.Ec2_Eip.create_nat_gateway(SubnetId=self.subnet.id,AllocationId=self.V_Eip['AllocationId'])
		logging.info("NATGATEWAY created successfully")
		time.sleep(5)
        	print self.natgw.id
	def associate_route(self):
		logging.info("associating route tables to subnet")
		pub_router1=""
		sub_router1=""
		pub_router2=""
		sub_router2=""
		for key,value in self.v_data["aws_vpc"].iteritems():
			if key == 'router':
 				pub_router1 = value['router1']['private']
 				pub_router2 = value['router2']['private']
			if key == 'subnet':
 				sub_router1 = value['subnet1']['private']
 				sub_router2 = value['subnet2']['private']
			if pub_router1 and sub_router1 and pub_router1 == "True":
			#	print pub_router1
				v_sub=boto3.client("ec2")
				v_subnet=v_sub.describe_subnets()
				for v_sub_check in range(len(v_subnet["Subnets"])):
					state=v_subnet["Subnets"][v_sub_check]["Tags"][0]["Value"]
					print state
					state_id=v_subnet["Subnets"][v_sub_check]['SubnetId']
					print state_id
					if state == "client_1_pubsubnet1" :
					   logging.info ("associating public subnet to public route")
					   for route_id in self.route_list:
					       print route_id
				  	          #self.route_table.associate_with_subnet(RouteTableId='string',SubnetId=state_id)
						
			if pub_router2 and sub_router2 and pub_router2 == "False":
				print pub_router2
			#	route_table.associate_with_subnet(SubnetId=subnet.id)
#			self.v_routertype=self.v_data["aws_vpc"]["router"]["v_router"]["private"]
#			self.v_subnettype=self.v_router["aws_vpc"]["subnet"]
		

s=aws_vpc()
s.vpc_create()
s.subnet_create()
#s.igw_create()
#s.attach_igw()
s.route_create()
#s.create_eip()
#s.create_natgw()
#s.associate_route()
