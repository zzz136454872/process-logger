# cpu 运行监测工具

## 功能
显示cpu占用信息，对于超过一定阈值的进程信息进行记录，可以同步记录到文件。
便于解决电脑不使用期间有软件莫名其妙占用系统资源导致风扇狂转的问题。

## 需要的package

pstuils

项目已经添加`requirements.txt`。
安装依赖文件。

```sh
pip install -r requirements.txt
```

## 配置信息
* cpuinfo=True 显示cpu信息
* refresh = 5  刷新时间（秒） 
* toFile=True  是否输出到文件
* filename='cpu_use.log' 输出的文件名
* hold=5       占用比例高于多少时进行记录
* rounds = 0   工作轮数，0 -> 一直工作


## contact

我的邮箱是 zzz136454872@163.com
