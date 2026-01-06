#!/data/data/com.termux/files/usr/bin/python3

import os
import subprocess
from datetime import datetime
import time
def get_storage_usage(): 
  #Return storage in percentage 
  result = subprocess.run(['df', '/data'], capture_output =True,text=True)
  lines=result.stdout.splitlines()  
  if len(lines)>=2:
    usage= lines[1].split()[4]
    return f'{usage}'
  return "N/A"



def get_battery_level():
#Return battery level as a percentage
  result = subprocess.run(['/data/data/com.termux/files/usr/bin/termux-battery-status'], capture_output=True, text=True)
  lines=result.stdout.splitlines()
  for line in lines:
    if '"percentage"' in  line:
      percentage=line.strip().split(':')[1].strip().replace(",","").replace("'","")
      return (f'{percentage}%') 
  return 'N/A'

def system_log():
#Get system log
  storage = get_storage_usage()
  battery= get_battery_level()
  message =f'Storage Used:{storage} | Battery:{battery}'
  subprocess.run([
    "/data/data/com.termux/files/usr/bin/termux-notification",
    "--title", "System Log",
    "--content", message
])
  log_system = "/data/data/com.termux/files/home/mini_tasks/system_log.txt"
  now =datetime.now().strftime('%d-%m-%Y %H:%M:%S')      
  log=f'[{now}] Storage Used: {storage}| Battery:{battery}'
  with open(log_system,'a')as f:
    f.write(log)
  
if __name__=='__main__':
  system_log()
  
