import os, time, socket, paramiko, logging
id=os.getlogin()
ip_addr=raw_input("Please enter the IP/hostname:")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(3)
logging.basicConfig(level=logging.DEBUG,filename="log.1",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)


class config():
        def __init__(self):
                self.s_name = raw_input("Please enter the serivce name: ")
                self.choice = int(raw_input("\nEnter the value either 1/2/3/4\n1. Status of the Process \n2. Start the Process\n3. Re-start the Process\n4. Stop the Process\n5. Quit\n\n "))
					
		try:
			s.connect((ip_addr,22))
			logging.info("{} User is connected to {} with ssh port".format(id,ip_addr))
		except:
			logging.error("{}, is NOT Connecting.".format(ip_addr))
			quit()
			
	def choose(self):
		remote_conn_pre = paramiko.SSHClient()
		remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		remote_conn_pre.connect(ip_addr)

		if self.choice == 1:
			stdin, stdout, stderr= remote_conn_pre.exec_command("ps -aef | grep -i "+self.s_name+" | grep -v 'grep' " )
			read1=stdout.read().strip()
			time.sleep(2)
			if read1:
				stdin, stdout, stderr= remote_conn_pre.exec_command("service "+self.s_name+" status")
				read2=stdout.read().strip()
				if read2:
					logging.info("{},Process is Running and Service status is Active.".format(self.s_name))
				else:
					logging.warn("{},Process is Running , but NOT in system service.".format(self.s_name))
			else:
				logging.error("{},is NOT running".format(self.s_name))
		elif self.choice == 2:
			logging.info("Starting the Service {}....\nPlease wait...".format(self.s_name))
			stdin, stdout, stderr= remote_conn_pre.exec_command("service "+self.s_name+" start")
			read1=stdout.channel.recv_exit_status()
			time.sleep(2)
			if read1 == 0:
				logging.info("{},Started sucessfully.".format(self.s_name))
			else:
				logging.error("Failed to start {}.".format(self.s_name))

		elif self.choice == 3:
			logging.info("Re-Starting the Service {}..\nPlease wait...".format(self.s_name))
			stdin, stdout, stderr= remote_conn_pre.exec_command("service "+self.s_name+" restart")
			time.sleep(2)
			read1=stdout.channel.recv_exit_status()
			if read1 == 0:
				logging.info("Restarted Sucessfully {}".format(self.s_name))
			else:
				logging.error("Failed to restart {}.".format(self.s_name))

                elif self.choice == 4:
			logging.info("Stopping the Service {} ....\nPlease wait...".format(self.s_name))
                        stdin, stdout, stderr= remote_conn_pre.exec_command("service "+self.s_name+" stop")
                        read1=stdout.channel.recv_exit_status()
                        time.sleep(2)
                        if read1 == 0:
				logging.info("{} Stopped sucessfully.".format(self.s_name))
                        else:
				logging.error("Failed to stop {}".format(self.s_name))


			
		elif self.choice == 5:
			print "Thank You."
			quit()

c=config()
c.choose()	
