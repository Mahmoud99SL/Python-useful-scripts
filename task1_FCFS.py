import matplotlib.pyplot as plt

def calculate_times(arrival_times, burst_times):
    n = len(arrival_times)
    
    # Initialize waiting time and turnaround time lists
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculate waiting time and turnaround time
    for i in range(n):
        if i == 0:
            waiting_time[i] = 0
        else:
            waiting_time[i] = max(0, waiting_time[i-1] + burst_times[i-1] - arrival_times[i])
        
        turnaround_time[i] = waiting_time[i] + burst_times[i]

    return waiting_time, turnaround_time

def calculate_average_times(waiting_time, turnaround_time):
    n = len(waiting_time)
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    return avg_waiting_time, avg_turnaround_time

def plot_gantt_chart(processes, arrival_times, burst_times):
    n = len(processes)
    
    # Calculate start and finish times for Gantt chart
    start_times = [0] * n
    finish_times = [0] * n
    
    for i in range(n):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(finish_times[i-1], arrival_times[i])
        
        finish_times[i] = start_times[i] + burst_times[i]
    
    # Plotting the Gantt chart
    plt.figure(figsize=(10, 5))
    plt.barh(processes, [burst for burst in burst_times], left=start_times, color='skyblue')
    
    # Adding labels and titles
    plt.xlabel('Time')
    plt.ylabel('Processes')
    plt.title('Gantt Chart for FCFS Scheduling')
    
    # Adding time annotations
    for i in range(n):
        plt.text(start_times[i] + burst_times[i]/2, i, f'P{i+1}', ha='center', va='center', color='black')
    
    plt.xticks(range(0, int(max(finish_times)) + 1))
    plt.grid(True)
    plt.show()

def main():
    # User input for number of processes
    n = int(input("Enter Processes number for simulation: "))
    
    processes = []
    arrival_times = []
    burst_times = []
    
    # Input arrival times and burst times
    for i in range(n):
        process_name = f"P{i+1}"
        processes.append(process_name)
        arrival_time = int(input(f"Enter arrival time for {process_name}: "))
        burst_time = int(input(f"Enter burst time for {process_name}: "))
        
        arrival_times.append(arrival_time)
        burst_times.append(burst_time)

    # Calculate waiting and turnaround times
    waiting_time, turnaround_time = calculate_times(arrival_times, burst_times)

    # Calculate average times
    avg_waiting_time, avg_turnaround_time = calculate_average_times(waiting_time, turnaround_time)

    # Output results
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

    # Plot Gantt chart
    plot_gantt_chart(processes, arrival_times, burst_times)

if __name__ == "__main__":
    main()