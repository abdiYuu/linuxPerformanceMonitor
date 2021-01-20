#!/usr/bin/python3
#Abdirahman & Jason
#linuxPerformanceMonitor.py

#import modules
import os, sys
import time

#display menu options

os.system("clear")
os.system('echo $USER')
print(time.strftime('%b/%d/%Y'))

print("Performance Monitor Started!\nChoose an option for more detailed information:\nMemory\nDrives\nUsers\nNetwork\nProcesses\nErrors\nPress'h' for help or 'q' to exit\n")

def mystar():
	arystar = "*" * 64
	print (arystar)

def errormessage():
	print("Error, invalid input, please select again\n")
	
i=0

while True:
	monitor = input("\nWhat would you like to monitor?\nMemory, Drives, Users, Network, Processes, or Errors\nPress 'h' for help or 'q' to exit: ")
	monitor = monitor.lower()
	os.system("clear")
	print("\n")
	
	if monitor == 'memory':
		print("Current Memory Information:\n")
		memfile = '/proc/meminfo'
		i=i+1
		x = 0
		mem = []
		with open (memfile, 'r') as infile:
			for x in range(3):
				lines = (infile.readline())
				print (lines)
				mem.append(lines)
			mystar()	
			option = input("Would you like to write this to a file? ")	
			
			
			if option == "yes":	
				memoryfile = input('Enter the filename you want to send these results to: ')
				print("Writing...")
				time.sleep(2)
				with open (memoryfile, 'a+') as outfile:
					outfile.write("Current Memory Information:\n")						
					for item in mem:
						outfile.write(item)
					outfile.write("\n")
					print("Thank you for your patience, your file {} is now ready!".format(memoryfile))
			elif option == "no":
				time.sleep(0.25)
					
			else:
				errormessage()		
				
				

	elif monitor == 'network':
		i=i+1
		print("Network Info\n")
		os.system("echo IP Address: ; hostname -I | awk '{print $1}'")
		print()
		os.system("echo Subnet Mask: ; /sbin/ifconfig eth0 | grep Mask | cut -d"':'" -f4")
		mystar()
		option = input("Would you like to write this to a file? ")
		if option == "yes":	
			networkfile = input('Enter the filename you want to send these results to: ')
			print("Writing...")
			time.sleep(2)
			with open (networkfile, 'a+') as outfile:
				os.system ("echo Current Network Configuration >> %s" % networkfile)
				os.system ("echo IP Address: >> %s" % networkfile)
				os.system ("hostname -I | awk '{print $1}' >> %s" % networkfile) 
				os.system ("echo Subnet Mask: >> %s" % networkfile)
				os.system ("/sbin/ifconfig eth0 | grep Mask | cut -d"':'" -f4 >> %s" % networkfile)
				outfile.write("\n")
				print("Thank you for your patience, your file {} is now ready!".format(networkfile))
						
		elif option == "no":
			time.sleep(0.25)
					
		else:
			errormessage()
		
	
		
		
	elif monitor == 'users':
		i=i+1
		print("User Info")
		os.system ("w | awk '{ print $1,$4 }' | awk '{if(NR>1)print}'")
		mystar()
		option = input("Would you like to write this to a file? ")	
			
		if option == "yes":	
			userfile = input('Enter the filename you want to send these results to: ')
			print("Writing...")
			time.sleep(2)
			with open(userfile, 'a+') as outfile:
				os.system ("w | awk '{ print $1,$4 }' | awk '{if(NR>1)print}' >> %s" % (userfile))
				outfile.write("\n")
				print("Thank you for your patience, your file {} is now ready!".format(userfile))
				
		elif option == "no":
				time.sleep(0.25)
					
		else:
			errormessage()			


		
	elif monitor == 'processes':
		print("Process Info")
		i=i+1
		processinfo = input("Would You Like a Summary(1) or a Detailed Look(2)? ")
		if processinfo == '1':
			os.system ("top -b -n 90 | head -n3")
			mystar()
			option = input("Would you like to write this to a file? ")
			if option == "yes":	
				processfile = input('Enter the filename you want to send these results to: ')
				print("Writing...")
				time.sleep(2)
				with open (processfile, 'a+') as outfile:
					os.system ("echo Process Summary >> %s" % processfile)
					os.system ("top -b -n 90 | head -n5 >> %s" % (processfile))
					outfile.write("\n")
					print("Thank you for your patience, your file {} is now ready!".format(processfile))
					
			elif option == "no":
				time.sleep(0.25)
					
			else:
				errormessage()
			
		
		elif processinfo == '2':
			os.system ("ps -aux")
			mystar()
			option = input("Would you like to write this to a file? ")
			if option == "yes":	
				detailedprocessfile = input('Enter the filename you want to send these results to: ')
				print("Writing...")
				time.sleep(2)
				with open (detailedprocessfile, 'a+') as outfile:
					os.system ("echo Process Summary >> %s" % detailedprocessfile)
					os.system ("top -b -n 90 | head -n5 >> %s" % (detailedprocessfile))
					outfile.write("\n")
					print("Thank you for your patience, your file {} is now ready!".format(detailedprocessfile))
			
			
			
			
			
			
		
	elif monitor == 'errors':
		i=i+1
		print("Loading Error Logs...\n")
		time.sleep(2)
		os.system("ls /var/log")
		logfile = input("Enter the filename of the log you'd like to view: ")
		
		if os.path.exists("/var/log/{}".format(logfile)):
			
			if os.path.isdir("/var/log/{}".format(logfile)):
				print("Your input leads to a directory. Now displaying...")
				time.sleep(2)
				os.system("ls /var/log/{}".format(logfile))
				filewithin = input("Enter the filename of the log you'd like to view: ")
				if filewithin.endswith('.gz'):
					print("Gzip file detected, unzipping...\n")
					time.sleep(2)
					unzippedfile = input("What would you like to name the unzipped file?: ")
					os.system ("gunzip < /var/log/{}/{} > {}".format(logfile, filewithin, unzippedfile))
					openoption = input("Would you like to ''display'' or ''open'' the file?: ")
        
					if openoption == 'open':
						os.system("gedit {}".format(unzippedfile))
            
					elif openoption == 'display':
						os.system("cat {}".format(unzippedfile))
            
					else:
						break
        
			elif logfile.endswith('.gz'):
				print("Gzip file detected, unzipping...\n")
				time.sleep(2)
				unzippedfile = input("What would you like to name the unzipped file?: ")
				os.system ("gunzip < /var/log/{} > {}".format(logfile, unzippedfile))
				openoption = input("Would you like to ''display'' or ''open'' the file?: ")
        
				if openoption == 'open':
					os.system("gedit {}".format(unzippedfile))
            
				elif openoption == 'display':
					os.system("cat {}".format(unzippedfile))
            
				else:
					break
        	
			else: 
				openoption2 = input("Would you like to ''display'' or ''open'' the file?: ")
				if openoption2 == 'open':
					os.system("gedit /var/log/{}".format(logfile))
            
				elif openoption2 == 'display':
					os.system("cat /var/log/{}".format(logfile))
                
				else:
					errormessage()
		else:
			print("Error, that file or directory doesn't exist, please try again...\n")	
	
	
	
	elif monitor == 'drives':
		i=i+1
		print ("Current Drive Information")
		os.system("df -h | awk NR==1")
		os.system("df -h | awk NR==2")
		mystar()
		option = input("Would you like to write this to a file? ")	
	
		if option == "yes":	
			drivefile = input('Enter the filename you want to send these results to: ')
			print("Writing...")
			time.sleep(2)
			with open (drivefile, 'a+') as outfile:
				os.system ("echo Current Drive Information >> %s" % drivefile)
				os.system ("df -h | awk NR==1 >> %s" % drivefile)
				os.system ("df -h | awk NR==2 >> %s" % drivefile)
				outfile.write("\n")
				print("Thank you for your patience, your file {} is now ready!".format(drivefile))
						
		elif option == "no":
			time.sleep(0.25)
					
		else:
			errormessage()
							
									

	elif monitor == 'h':
		print('NAME:\n%50s'%('perfmon - a performance monitoring program'))
		print('SYNOPSIS:\n%15s'%('perfmon'))
		print('DESCRIPTION:\n%179s'%('The perfmon program monitors system performance and displays information on various real-time 		performance data such as CPU, disk, network, memory, users, and system errors'))
		
	elif monitor == 'q':
		os.system("clear")
		print ("You used the PerfMon %d time(s)" %i)
		print("Now exiting Performance Monitor...")
		time.sleep(2)
		print("Done!")
		sys.exit()
	else:
		errormessage()

