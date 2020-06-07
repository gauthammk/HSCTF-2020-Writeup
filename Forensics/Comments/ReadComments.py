import os

os.system("zipdetails Comments.zip | grep Comment")
os.system("unzip Comments.zip")
for i in range(1, 9):
    os.system("zipdetails " + str(i) + ".zip | grep Comment")
    os.system("unzip " + str(i) + ".zip")
