import os
path='/data/data/com.termux/files/home/python_codes' 
def scan_file():
  try:
    count=0
    for file in os.listdir(path):
      full_path=os.path.join(path,file)
      if os.path.isdir(full_path):
        continue
      size = os.path.getsize(full_path)
      size_in_bytes=size/(1024*1024)
      with open('file_scanner.txt','a')as f: 
        f.write (f'{file}{size_in_bytes:.6f}MB\n')
    print ('✓File logged successfully')
    if size_in_bytes > 5:   
      print ('File larger than 5MB')
  except Exception as e:
    print (f'Error: {e}')
scan_file()
