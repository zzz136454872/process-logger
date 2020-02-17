from psutil import *
from time import sleep
from logging import getLogger, FileHandler, info, StreamHandler,INFO,DEBUG

#config 
cpuinfo=True
refresh = 5
toFile=False
filename='log.txt'
hold=10

logger=getLogger()
logger.setLevel(DEBUG)
console=StreamHandler()
console.setLevel(INFO)
logger.addHandler(console)


if toFile:
    filehandler=FileHandler(filename, mode='w')
    filehandler.setLevel(INFO)
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

while(True):
    info("round: %d",i)
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
                info('pid: ',pid)
                info('进程名称: %s', ps[pid].name())          #进程名称
                #info('运行状态:', p.status())        #当前状态
                #info('创建时间:', p.create_time())   #创建时间
                info('CPU信息: %d',  ps[pid].cpu_times())     #进程的cpu时间信息,主要：user,system运行时间
                info('CPU时间: %d', tmp_time)
                #info('内存信息:', p.memory_percent())#进程内存利用率
                #info('内存使用:', p.memory_info())   #进程内存使用详情
                #info('IO信息：', p.io_counters() )   #进程的IO信息,包括读写IO数字及参数
                #info('线程数：', p.num_threads() )   #进程开启的线程数
                info()
        except Exception:
            info("now")
            continue
    sleep(refresh)



