# CPU Scheduling - FCFS & SJF (Non-Preemptive)


class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# ----------- FCFS -----------
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0

    print("\n--- FCFS Scheduling ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        if time < p.at:
            time = p.at  # CPU idle condition

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    avg_wt = sum(p.wt for p in processes) / len(processes)
    avg_tat = sum(p.tat for p in processes) / len(processes)

    print("Average WT:", avg_wt)
    print("Average TAT:", avg_tat)


# ----------- SJF (Non-Preemptive) -----------
def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n

    print("\n--- SJF Scheduling ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if processes[i].at <= time and not visited[i]:
                if processes[i].bt < min_bt:
                    min_bt = processes[i].bt
                    idx = i

        if idx == -1:
            time += 1
            continue

        p = processes[idx]
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        visited[idx] = True
        completed += 1

        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    avg_wt = sum(p.wt for p in processes) / n
    avg_tat = sum(p.tat for p in processes) / n

    print("Average WT:", avg_wt)
    print("Average TAT:", avg_tat)


# ----------- INPUT -----------
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = f"P{i+1}"
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    processes.append(Process(pid, at, bt))

# Display Input
print("\nInput Processes:")
print("PID\tAT\tBT")
for p in processes:
    print(f"{p.pid}\t{p.at}\t{p.bt}")

# Run FCFS
fcfs([Process(p.pid, p.at, p.bt) for p in processes])

# Run SJF
sjf([Process(p.pid, p.at, p.bt) for p in processes])


# ------------- GANTT CHART ---------------
def gantt_chart(processes):
    print("\nGantt Chart:")
    
    print("|", end="")
    for p in processes:
        print(f" {p.pid} |", end="")
    
    print("\n0", end="")
    for p in processes:
        print(f"    {p.ct}", end="")




# ----------- PERFORMANCE ANALYSIS AND COMPARISON ---------------
def compare_algorithms(fcfs_processes, sjf_processes):
    fcfs_avg_wt = sum(p.wt for p in fcfs_processes) / len(fcfs_processes)
    fcfs_avg_tat = sum(p.tat for p in fcfs_processes) / len(fcfs_processes)

    sjf_avg_wt = sum(p.wt for p in sjf_processes) / len(sjf_processes)
    sjf_avg_tat = sum(p.tat for p in sjf_processes) / len(sjf_processes)

    print("\n--- Performance Comparison ---")
    print(f"FCFS Average WT: {fcfs_avg_wt}")
    print(f"FCFS Average TAT: {fcfs_avg_tat}")

    print(f"SJF Average WT: {sjf_avg_wt}")
    print(f"SJF Average TAT: {sjf_avg_tat}")

    # Comparison Logic
    if sjf_avg_wt < fcfs_avg_wt:
        print("\nSJF is better than FCFS (Lower Waiting Time)")
    elif sjf_avg_wt > fcfs_avg_wt:
        print("\nFCFS is better than SJF")
    else:
        print("\nBoth algorithms have same performance")

    print("\nConclusion:")
    print("SJF minimizes waiting time but may cause starvation.")
    print("FCFS is simple but less efficient.")





# Run FCFS
fcfs_processes = [Process(p.pid, p.at, p.bt) for p in processes]
fcfs(fcfs_processes)

# Run SJF
sjf_processes = [Process(p.pid, p.at, p.bt) for p in processes]
sjf(sjf_processes)

# Compare both
compare_algorithms(fcfs_processes, sjf_processes)
