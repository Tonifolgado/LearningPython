import os
# Specify the path to count files and directories
PATH = "/Users/antonioalvarezfolgado/Folgado/eLearning/LearningPython"
files, dirs = 0, 0

for root, dirnames, filenames in os.walk(PATH):
    print('Looking in:', root)
    dirs += len(dirnames)
    files += len(filenames)

print('Files:', files)
print('Directories:', dirs)
print('Total:', files + dirs)

# List of Running Processes
import psutil
# Iterate over all running processes
print(f"{'PID':<10} {'Name':<40} {'Status':<10} {'username':<10}")
print("-" * 70)
for proc in psutil.process_iter(['pid', 'name', 'status', 'username']):
    try:
        pid = proc.info['pid']
        name = proc.info['name'] or "N/A"
        status = proc.info['status'] or "N/A"
        username = proc.info['username'] or "N/A"
        
        print(f"{pid:<10} {name:<40} {status:<10} {username:<10}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    