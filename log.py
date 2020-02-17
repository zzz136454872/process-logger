from psutil import *
from time import sleep
from logging import getLogger, FileHandler, info, StreamHandler,INFO,DEBUG,Formatter

#config 
cpuinfo=True # show cpu info 
refresh = 5  # time before refresh 
toFile=True  # log to file
filename='cpu_use.log' # log file name (does not work when toFile = False)
hold=5       # the minimal cpu percent to log
rounds = 0 # work rounds 0 => inf

logger=getLogger()
logger.setLevel(DEBUG)
console=StreamHandler()
console.setLevel(INFO)
formatter = Formatter("%(asctime)s - %(message)s")
console.setFormatter(formatter)
logger.addHandler(console)

if toFile:
    filehandler=FileHandler(filename, mode='w')
    filehandler.setLevel(INFO)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

if cpuinfo:
    info("CPU核心数量: "+str(cpu_count(logical=False))) # CPU物理核心
    info("CPU线程数量: "+str(cpu_count())) # CPU逻辑数量
    #获取CPU不同状态运行时间
    info(cpu_times())
    info('CPU 执行用户进程时间：'+str( cpu_times().user))
    info('CPU 执行系统调用时间：'+str( cpu_times().system))
    info('CPU 空闲等待    时间：'+str( cpu_times().idle))
    info('CPU 响应中断   时间：'+str( cpu_times().interrupt))
    #CPU使用率：不加参数为上一次调用到现在使用率
    info('CPU      使用率：'+str(cpu_percent()))
    #3秒内CPU使用率
    info('CPU  3秒内使用率：'+str(cpu_percent(interval=3)))
    #3秒内每个CPU使用率
    info('每个逻辑CPU使用率：'+str(cpu_percent(percpu = True)))
    #CPU各个状态使用情况（百分比）
    info('CPU 各个状态使用情况：'+str(cpu_times_percent()))
    #每个CPU各个状态使用情况
    info('各个CPU 各个状态使用情况:')
    cpuinfos = cpu_times_percent(percpu = True)
    for cpuinfo in cpuinfos:
        info(cpuinfo)

ps=[0 for i in range(65536)]
i=0

pid_list = pids()
for pid in pid_list:
    if(ps[pid]==0):
        p=Process(pid)
        ps[pid]=p
    ps[pid].cpu_percent()

if rounds == 0:
    rounds=1<<63 # not good but very simple 

for round in range(rounds):
    #info("round: %d",i)
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
            if(tmp_time > hold):
                info('pid: '+str(pid))
                info('进程名称: '+str( ps[pid].name()))          #进程名称
                #info('运行状态:'+str( p.status()))        #当前状态
                #info('创建时间:'+str( p.create_time()))   #创建时间
                info('CPU信息: '+str(  ps[pid].cpu_times()))     #进程的cpu时间信息+str(主要：user+str(system运行时间
                info('CPU时间: '+str( tmp_time))
        except Exception as e:
            info("an execption occured!")
            print(e.message)
            continue
    sleep(refresh)


