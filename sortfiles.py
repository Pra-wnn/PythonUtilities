import os
import shutil

def organize(path):
    os.chdir(path)
    lis = os.listdir()

    for i in lis:
        (filename,ext) = os.path.splitext(i)
        if ext == "":
            continue
        else:
            
            if ext.endswith(('.jpg','.jpeg','.png','.gif','.htm','.webp')):
                # use tuple for more than 3 arguments ends with
        
                if not os.path.exists("PicturesAnime"):
                    os.mkdir("PicturesAnime")
                shutil.move(i,path+"\\"+"PicturesAnime"+"\\")
            elif ext.endswith(('.html','.pdf','.txt')):
           
                if not os.path.exists("Otherfiles"):
                    os.mkdir("Otherfiles")
                shutil.move(i,path+"\\"+"Otherfiles"+"\\")
            
            elif ext.endswith('.mp4'):
              
                if not os.path.exists("mp4s"):
                    os.mkdir("mp4s")
                shutil.move(i,path+"\\"+"mp4s"+"\\")
            elif ext.endswith(('.mkv','.webm','.rar')):
                # print(ext)
                direct = 'directory'
                parent = 'D:\\'
                path1 = os.path.join(parent,direct)
                os.makedirs(path1,exist_ok=True)   
                #  pls use this if u want abs path done and check if it exists or not
                # print(i)
                shutil.move(i,path1)
                # print(path1)

    print("Files Organized Sucessfully")

path = input("Enter path of the directory to organize: ")

if os.path.exists(path):
    organize(path)
else:
    print("Path Doesn't exist")
