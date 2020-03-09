import os

os.getcwd()

for name in os.listdir("train33/"):
    if name.endswith("jpg"):
       name,mid,exe  = name.split(".")
       print(name)