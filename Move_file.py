import os;
import shutil;
from_dir="C:/Users/agusm/pro102/document_files"
to_dir="C:/Users/agusm/pro102/document_files"

list_files=os.listdir(from_dir)
for i in list_files:
    name,ext=os.path.splitext(i)
    if ext=='':
        continue
    if ext in ['.pdf','.docx','.doc','.txt']:
        path1 = from_dir+'/'+i
        path2 = to_dir+'/'+'filesss'
        path3 = to_dir+'/'+'filesss'+i
    if os.path.exists(path2):
        print("Moving"+i+".....")
        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("Moving"+i+".....")
        shutil.move(path1,path3)
