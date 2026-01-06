import os
import shutil
import json
from logger import log_action
from notifier import notify

path = "/data/data/com.termux/files/home/storage/downloads"
with open("file_types.json") as f:
  file_types= json.load(f)
def organize_downloads(): 
  scanned = 0
  moved_count=0
  uncategorized=0
  backup_folder=os.path.join(path,"backup")
  os.makedirs(backup_folder,exist_ok=True)
  for file in os.listdir(path):
    file_path=os.path.join(path,file)
    if not os.path.isfile(file_path):
      continue
    if file.endswith(".tmp") or file.endswith(".crdownload"):
      continue
    scanned+=1
    ex=file.split(".")[-1].lower()
    moved=False
    for category,extensions in file_types.items():
      if ex in extensions:
        des_folder = os.path.join(path,category)
        os.makedirs(des_folder,exist_ok=True)
        try:
          shutil.copy(file_path,
          os.path.join(backup_folder,file))
          shutil.move(file_path,
          os.path.join(des_folder,file))   
          log_action(f'Moved {file} to {des_folder}')
          notify("file_organizer",f"{file} moved to {category}")
          moved_count+=1
          moved =True
        except Exception as e:
            log_action(f'Error moving {file}:{e}')
        break
    if not moved:
      uncategorized+=1
  print (f'Total file scanned:{scanned}')  
  print (f'File moved:{moved_count}')
  print (f'Uncategorized:{uncategorized}')
if __name__ =="__main__":
  organize_downloads()
