import boto3
import json

class aws_vpc:
        def __init__(self):
            self.ec2=boto3.resource("ec2")
            fp=open("network.json")
            self.v_data=json.load(fp)
            fp.close()
                
        def vpc_create(self):
            v_vpcname=self.v_data["aws_vpc"]["vpc"]["vpcname"]
            v_vpccidr=self.v_data["aws_vpc"]["vpc"]["vpccidr"]
            self.v_vpc=self.ec2.create_vpc(CidrBlock=v_vpccidr)
            self.v_vpc.create_tags(Tags=[{"Key":"Name","Value":v_vpcname}])
            
        def subnet_create(self):
	    for v_sub in self.v_data["aws_vpc"]["subnet"]:
		v_subnetname=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_name"]
		v_subnetcidr=self.v_data["aws_vpc"]["subnet"][v_sub]["sub_cidr"]
		subnet = self.ec2.create_subnet(CidrBlock=v_subnetcidr, VpcId=self.v_vpc.id)
		subnet.create_tags(Tags=[{"Key":"Name","Value":v_subnetname}])
s=aws_vpc()
s.vpc_create()
s.subnet_create()
