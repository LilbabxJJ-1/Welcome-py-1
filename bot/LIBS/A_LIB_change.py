import os
import sys
import json 
sys.path.append('/home/dev/busboy/bot/LIBS')
os.chdir('/home/dev/busboy/bot/LIBS')
array=[]
LOCAL=globals()
def FIND_DATA(FIND):
  with open('JSON/file.json', 'r') as f: 
    data = json.load(f)
    data=data["data"]
    LOCAL["datax"]=data
    f.close()
  LOCAL["ids"] = [] 
  for piece in data:
    name = piece['name'] 
    ID = piece['id']
    ids.append(name)
    ids.append(ID)    

  for x in range(len(ids)):
    if ids[x] == FIND:
      return x+1

def WRITE_SYSTEM(z, b):
  key=ids[z-1]
  text={}
  limit=len(ids)
  for x in range(len(datax)):
    z=datax[x]
    if z==key:
      LOCAL['num']=x+1
  datax[num]=b
  print(datax)
  return
    
  MAIN = {'data': [text]}
  print(MAIN)
  f=open('JSON/file.json', 'w')
  json.dump(MAIN, f)
  f.close() 

def main(start_core, MAIN_CORE, TEXT):
  if MAIN_CORE == "w": 
    MAIN_CORE=False
  elif MAIN_CORE == "r":
    MAIN_CORE=True
  if MAIN_CORE:
    x=FIND_DATA(start_core)
    return ids[x]
  aaax=FIND_DATA(start_core)
  return WRITE_SYSTEM(aaax, TEXT)




"""
start_core=command
main_core=r/w
text=text
"""
