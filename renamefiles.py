import os 

folder_path="/data/data/com.termux/files/home"
def rename():
  i=1
  for file in os.listdir(folder_path):
    if file.startswith("test"):
      oldpath=os.path.join(folder_path,file)
      newpath=os.path.join(folder_path,f"file_{i}")
      if os.path.exists(newpath):
        print (f'Skipped: {newpath} exists')
      else:
        print (oldpath,"'n",newpath) 
        os.rename(oldpath,newpath)
      i+=1  

rename()
