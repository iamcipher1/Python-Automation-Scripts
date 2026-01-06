from datetime import datetime
import time
import os

def  reminder():
  now= datetime.now().strftime('%d-%m-%Y %H:%M:%S')
  return f'[{now}] Reminder: Keep learning and hackin[ (termux.notification--- title 'Daily Reminder'---content '{message)'

def send_notification():
os.system(f'Termux notification --> title: Daily_Reminder | Content:{message}')

def main1():
  home='/data/data/com.termux/files/home/daily_note.txt'
  
  print ('Daily reminder Script started...')
  while True:
   message = reminder()
   with open('daily_note.txt','w')as f:
      f.write(message)
      
    with open('daily_note.txt','r')as f:
      print ('Fresh log:', f.read())
    send_notification(message)
    time.sleep(10)
if __name__=='__main__':
  main1()




