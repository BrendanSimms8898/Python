#Brendan Simms is the main author of this file
#I, Brendan Simms, acknowledge and promise to adhere to the conditions of the DCU integrity policy

import sys
import list
import schedule_sjf
import priority_schedule
import schedule_fcfs
import schedule_rr


if __name__ =="__main__":
	ListofTasks = [] #Assign an empty list


	try: #try to open file 
		file = open(sys.argv[1], 'r') #open file with read premissions

	except FileNotFoundError: #expect FileNotFoundError and print error message
		print("Error file not found") #error message

	finally: #Finally do this 
		contents = file.read().splitlines() # set variable contents to split lines in file
		file.close() 
		for line in contents: #for loop for line in contents which was assigned vallue of individual file lines previously 
			line = line.split(', ') # Split line by ', ' and assign new_line variable to it 
			Name = line[0]
			Priority = int(line[1])
			Burst = int(line[2])
			ListofTasks.append((Name, Priority, Burst)) #Assigns tuple to Name, Priority, Burst
#Executes from schedule_sjf file
	schedule_sjf.sjf_exe(ListofTasks) 
	schedule_sjf.AverageTime(ListofTasks)
#Executes from priority_schedule file
	priority_schedule.schedule_priorty_exe(ListofTasks)
	priority_schedule.AverageTime(ListofTasks)
#Executes from schedule_fcfs file
	schedule_fcfs.FirstComeFirstServed(ListofTasks)
	schedule_fcfs.AverageTime(ListofTasks)
#Executes from schedule_rr file
	schedule_rr.rr(ListofTasks)

