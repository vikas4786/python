class student:
	v_Iname="osrc"
	def __init__(self,v_name):
		self.name=v_name
		
	def fetch(self,v_objects):
		for i in v_objects:
			print i

v_ch="y"
l=[]
while v_ch == "y":
     v_input = raw_input("enter the name : ")
     s1=student(v_input)
     l.append(s1)
     v_ch=raw_input("do u want to continue(y)")

s1.fetch(l)
