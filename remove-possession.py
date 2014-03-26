'''
Created on 2014/3/25

@author: yufeilong
'''
#__version__ = '3.3.5'

import subprocess
import os

commond_netstat_list = "netstat -ano|findstr \"5037\""

commond_netstat_find = "tasklist|findstr"

commond_kill_task = "taskkill /f /t /im"

res = subprocess.Popen(commond_netstat_list, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = res.stdout.readlines()

print(result)

strlist = str(result).split('  TCP    ')

for value in strlist:
    if value.find('LISTENING') > 0:
        value.strip().lstrip()
#         commond_task_port = value[len(value)-10:len(value)-6]
        commond_task_port = value[len(value)-13:len(value)-9]
        print("commond_task_port::" + commond_task_port)
        commond_netstat_find += " \"" + commond_task_port + "\""
        print("commond_netstat_find" + commond_netstat_find)
        break

res_task = subprocess.Popen(commond_netstat_find, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

reult_task = res_task.stdout.readlines()

str_res_list = str(reult_task)[3:10]

print("str_res_list::" + str_res_list)

str_stop_task = "\"" + commond_kill_task + " " + str_res_list + "\""
 
print(str_stop_task)

os.system(str_stop_task)

os.system("adb start-server")

os.system("pause")

# result_code = os.system(str_stop_task)
 
# print(result_code)
