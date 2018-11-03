fp=open("monitoring.csv")
v_lines=fp.readlines()
number=1
d={"monitoring":{str(number):{"action":{"state":""}}}}
for v_line in v_lines:
	v_org=v_line.strip("\n")
	l=v_org.split("|")
	d["monitoring"][str(number)]["service"]=l[0]
	d["monitoring"][str(number)]["hostname"]=l[1]
	d["monitoring"][str(number)]["port"]=l[2]
	d["monitoring"][str(number)]["action"]["state"]=l[3]
	number=number+1
	d["monitoring"].update({str(number):{"action":{"state":""}}})
import json
fp=open("monitoring.json","w")
json.dump(d,fp)
