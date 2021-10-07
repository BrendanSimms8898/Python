#Brendan Simms is the main author of this file
#I, Brendan Simms, acknowledge and promise to adhere to the conditions of the DCU integrity policy

import CPU

def rr(ListofTasks):
	z = 0
	temp_burst = [] # create a new list
	quantum = 10
	waittime = 0
	turnaround = 0

	print("Round Robin:\n")
	
	for line in ListofTasks:
		temp_burst.append([line, line[2]]) #Add a new tuple including our original tuple followed by the cpu burst time

	lengthof = len(temp_burst) # Set lengthof as length of out new list
	while z < lengthof:  #while z is less than the length of temp_burst, to iterate through the list
		i = 0
		while i < lengthof: #while i is less than the length of temp_burst, iterates through the list 
			if temp_burst[i][1] <= quantum and temp_burst[i][1] != 0: #if new BurstTime creation is less than or = quantum which is = 10 	and 	while bursttime doesnt = 0
				waittime += temp_burst[i][1] #adds burst time to wait time 
				temp_burst[i][1] -= temp_burst[i][1] #minuses burst time by itself so it = 0 / This is used instead of -= quantum to prevent a negative burst time being assigned
				CPU.run(temp_burst[i][0], quantum) #Run the task for time value of quantum
				turnaround += waittime #Add wait time to turn around time

			elif temp_burst[i][1] > quantum: #otherwise if changable BurstTime is more than quantum time value

				waittime += quantum #Adds quantum to waittime
				temp_burst[i][1] -= quantum # Takes quantum away from changable burst time
				CPU.run(temp_burst[i][0], quantum) #Runs task for Quantum
			i += 1
		z += 1

	average_turnaround = turnaround / lengthof
	average_waittime = waittime / lengthof

	print("Average turnaround time: " + str(average_turnaround))
	print("Average wait time: " + str(average_waittime))