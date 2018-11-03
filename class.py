class student:
	v_iname="vikas"
	def __init__(self,v_name,v_age,v_phn,v_email):
		self.name=v_name
		self.age=v_age
		self.phn=v_phn
		self.email=v_email
class MCA(student):
	v_type="MCA"
	def store(self):
		pass
class BCA(student):
	v_type="BCA"
	def store(self):
		pass
class BTECH(student):
	v_type="BTECH"
	def store(self):
		pass
v_ch="y"
v_list=[]
while v_ch=="y":
	v_input=raw_input("enter the type of student(M/B/G)")
	if v_input == "M":
		obj=MCA(raw_input(),raw_input(),raw_input(),raw_input())
		v_list.append(obj)
	elif v_input == "B":
		obj=BCA(raw_input(),raw_input(),raw_input(),raw_input())
		v_list.append(obj)
	elif v_input == "G":
		obj=BTECH(raw_input(),raw_input(),raw_input(),raw_input())
		v_list.append(obj)
        v_ch=raw_input("Do u want to continue(y/n)")
def store(v_list):
	fp=open("student.csv","a")
	for i in v_list:
		fp.write(i.v_type+","+i.name+","+i.phn+","+i.email+"\n")
	fp.close()
store(v_list)
