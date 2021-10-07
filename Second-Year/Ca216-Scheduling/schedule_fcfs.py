#Brendan Simms is the main author of this file
#I, Brendan Simms, acknowledge and promise to adhere to the conditions of the DCU integrity policy

import CPU

def FirstComeFirstServed(ListofTasks):
	print("First Come First Served:\n")
	for line in ListofTasks:
		CPU.run(line, line[2])

def AverageTime(ListofTasks):
   i = 0 # assigning i variable a 0 value
   item_counter = len(ListofTasks) #assigning varibale item_counter the length of dictionary ListofTasks
   turnaround = 0
   total_waiting_time = 0
   total_turnaround_time = 0
   average_waiting_time = 0
   average_turnaround_time = 0 

   for line in ListofTasks: #Simple for loop iteration for list using tuples to iterate
      turnaround = total_waiting_time + line[2] #turnaround value is set to total waiting time + Burst time of line in ListofTasks
 #     print("current turnaround: " + str(turnaround))		Used for testing purposes
      total_turnaround_time += turnaround #total_turnaround_time value set to turnaround variable
 #     print("total turnaround: " + str(total_turnaround_time)) 	Used for Testing purposes
      if (i < (item_counter - 1)): # if statement to prevent last CPU burst being added to wait time as no process follows it
         total_waiting_time += line[2] # Let Total_waiting_time equal CPU burst of tuple for each iteration
 #        print("total wait: " + str(total_waiting_time)) 	Used ffor testing purposes
      i += 1

   average_waiting_time = total_waiting_time / item_counter # calculate average by dividing total_waiting_time by length of list
   average_turnaround_time = total_turnaround_time / item_counter # calculate average by dividing total_turnaround_time by length of list

   print("Average turnaround time: " + str(average_turnaround_time))
   print("Average waiting time: " + str(average_waiting_time)) + "\n"
