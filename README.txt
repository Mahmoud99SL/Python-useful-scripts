For Dr. Ghayth:
1- All tasks are written in Python.
2- Before Running any task, please make sure to have installed the matplotlib and numpy packages 
   since it was necessary to draw in tasks
3- if the libraries are not already installed on your device, follow these steps:
  	turn VPN(just in case), 
	then in windows command prompt (as adminstrator), 
	type the following commands:

		3.1-  python -m ensurepip --upgrade     // to install pip command

		3.2-  pip --version				      // to make sure pip is installed

		3.3-  python -m pip install -U matplotlib *or* pip install matplotlib    //to install matplotlib and numpy
------------------------------------------------------------------------
How to Run tasks in VSCode:
	1- Open the Folder BOS501_Task2 in VSCode.
	2- Open new terminal
	3- run the task you want(copy this to terminal):
		1-  python task1_FCFS.py
		2-  python task2_paging.py
		3-  python task3_Contiguous.py
		4- Enter input to your chosen task as shown below
 -----------------------------------------------------------------------
Task1: Process Scheduling Simulation (FCFS Algorithm) 
	How to run task1_FCFS.py  :
		1- Enter how many processes to simulate scheduling using FCFS
		2- Enter the arrival time and burst time of each process in sequential order
		3- The output should be: Average Turnaround Time, Average Waiting Time, Gantt chart sketch(using matplotlib)
		4- The program is easy to test so I did not include test input for task1.
-------------------------------------------------------------------------
Task2: Simulate a simple paging mechanism using programming
	How to run task2_paging.py :
		1- Enter size of physical memory
		2- Enter page size
		3- Enter sequence of page requests:
			Enter first number 
			then press spacee 
			enter second number.
			.
			.
			etc 
		4- an output should be: 
			page table (with a comment), 
			how many page faults in total, 
			illustration of memory state after each request using matplotlib
			Note: This input is described in technical simulation terms as:
					4 frames in physical memory (4 / 1 = 4)
					A varied sequence of page requests to test different aspects of the paging mechanism
	Test input: 
		Enter size of physical memory: 4
		Enter page size: 1
		Enter sequence of page requests (one per line): 0 1 2 3 0 1 4 0 2 3 0 4
			
	Expected output: 
		Here's what our Page Table looks like at the end:
		Page 0 is in Frame 3
		Page 1 is in Frame -1
		Page 2 is in Frame 2
		Page 3 is in Frame 3
		Page 4 is in Frame 3

		We had 6 Page Faults in total

		Illustration should appear to show memory state after each request.
----------------------------------------------------------------------------
Task3: File System Simulation
	How to run task3_Contiguous.py:
		1- Enter the number of files
		2- Enter sizes of each file
		3- Enter the total number of available disk blocks
	Test input:
		1- Enter the number of files: 3
		2- Enter size of file 1: 2
		   Enter size of file 2: 3
		   Enter size of file 3: 1
		   Enter the total number of available disk blocks: 6
	Expected Output:
	1- Allocation Table:
		Block 0: File 0
		Block 1: File 0
		Block 2: File 1
		Block 3: File 1
		Block 4: File 1
		Block 5: File 2
	2- A sketch of how files are stored in disk blocks(using matplotlib)
	

