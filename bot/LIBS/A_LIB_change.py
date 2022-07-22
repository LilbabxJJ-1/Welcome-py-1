import json
import os
import sys
FILE_PATH='/home/dev/busboy/bot/LIBS/'
sys.path.append(FILE_PATH)
os.chdir(FILE_PATH)

def WRITE_SYSTEM(placement, array, TEXT, data, cn):
  add=[]
  for x in range(len(data)):
    wrong_array=data[x]
    if cn != wrong_array["name"]:
      add.append(wrong_array)
    else:
      add.append({'name': cn, 'id': TEXT})
  MAIN = {'data': add}
  print(MAIN)
  with open(f'{FILE_PATH}JSON/file.json', 'w') as f:
    json.dump(MAIN, f)
    f.close() 
  #return add
  
  

def write(command_name, TEXT):
  cn=command_name
  with open(f'{FILE_PATH}JSON/file.json', 'r') as f: 
    data = json.load(f)
    data=data["data"]
    f.close()
  for x in range(len(data)):
    array=data[x]
    if cn == array["name"]:
      return WRITE_SYSTEM(x, array, TEXT, data, cn)
  
    
    
def read(FIND):
  with open(f'{FILE_PATH}LIBS/JSON/test.json', 'r') as f: 
    data = json.load(f)
    data=data["data"]
    f.close()
  ids = [] 
  for piece in data:
    name = piece['name'] 
    ID = piece['id']
    ids.append(name)
    ids.append(ID)    

  for x in range(len(ids)):
    if ids[x] == FIND:
      return ids[x+1]

