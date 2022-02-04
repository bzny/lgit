from datetime import datetime
import os

print('含有\n %s'%os.listdir(os.getcwd()))
os.remove('lss.txt')
print('删除后含有\n %s'%os.listdir(os.getcwd()))