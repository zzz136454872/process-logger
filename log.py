from psutil import *
from time import sleep

#config 
#refresh  = 5
#cpuInfo = False
#file = 'log.txt'
#Tofile = False


#print(cpu_count(logical=True))
#print(cpu_count(logical=False))
#print(cpu_times(percpu=False))
#print(cpu_percent(interval=None, percpu=False))
#print(cpu_times_percent(interval=None, percpu=False))
#
#sleep(1)
#
#print(cpu_count(logical=True))
#print(cpu_count(logical=False))
#print(cpu_times(percpu=False))
#print(cpu_percent(interval=None, percpu=False))
#print(cpu_times_percent(interval=None, percpu=False))
#
#import psutil
##获取CPU不同状态运行时间
#print(psutil.cpu_times())
#print('CPU 执行用户进程时间：', psutil.cpu_times().user)
#print('CPU 执行系统调用时间：', psutil.cpu_times().system)
#print('CPU 空闲等待    时间：', psutil.cpu_times().idle)
#print('CPU 响应中断   时间：', psutil.cpu_times().interrupt)
##CPU使用率：不加参数为上一次调用到现在使用率
#print('CPU      使用率：',psutil.cpu_percent())
##3秒内CPU使用率
##print('CPU  3秒内使用率：',psutil.cpu_percent(interval=3))
##3秒内每个CPU使用率
#print('每个逻辑CPU使用率：',psutil.cpu_percent( percpu = True))
##CPU各个状态使用情况（百分比）
#print('CPU 各个状态使用情况：',psutil.cpu_times_percent())
##每个CPU各个状态使用情况
#print('各个CPU 各个状态使用情况:')
#cpuinfos = psutil.cpu_times_percent(percpu = True)
#for info in cpuinfos:
#    print(info)
#
##1M = 1024*1024 
##1G = 1024*1024*1024
#M = 1024*1024 
#G = M * 1024
#mem = psutil.virtual_memory()
#print('系统内存：', mem)
#print('总  内存：%dM %fG'%(mem.total//M, mem.total/G))
#print('空闲内存：%dM %fG'%(mem.available//M, mem.available/G))
#print('使用内存：%dM %fG'%(mem.used//M, mem.used/G))
#print('未使用内存：%dM %fG'%(mem.free//M, mem.free/G))
#print('内存使用率：%d%%'% mem.percent)
#print('swap 内存：', psutil.swap_memory())
#
#print()

#主要信息：进程名，状态，创建时间，CPU内存使用情况，线程数
ps=[0 for i in range(65536)]
i=0

pid_list = pids()
for pid in pid_list:
    if(ps[pid]==0):
        p=Process(pid)
        ps[pid]=p
    ps[pid].cpu_percent()


while(True):
    print("round: ",i)
    i+=1
    pid_list = pids()
    for pid in pid_list:
        if(pid==0):
            continue
        try:
            if(ps[pid]==0):
                p=Process(pid)
                ps[pid]=p
            tmp_time=ps[pid].cpu_percent()
            if(tmp_time > 10):
                print('pid: ',pid)
                print('进程名称:', ps[pid].name())          #进程名称
                #print('运行状态:', p.status())        #当前状态
                #print('创建时间:', p.create_time())   #创建时间
                print('CPU信息:',  ps[pid].cpu_times())     #进程的cpu时间信息,主要：user,system运行时间
                print('CPU时间:', tmp_time)
                #print('内存信息:', p.memory_percent())#进程内存利用率
                #print('内存使用:', p.memory_info())   #进程内存使用详情
                #print('IO信息：', p.io_counters() )   #进程的IO信息,包括读写IO数字及参数
                #print('线程数：', p.num_threads() )   #进程开启的线程数
                print()
        except Exception:
            print("now")
            continue
    sleep(5)



