import pandas as pd
import os
import sys


#csv 폴더 탐색

os.chdir("./")
path = os.getcwd() + "/경로당"
#print(path)
filelist = os.listdir(path)

for x in filelist : 
    print(x)
    df = pd.read_csv(path+"/"+x)
    df.info()
    