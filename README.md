## 介绍

这些脚本主要用来画图和估算带宽，**注意本项目是python3的！**

## 数据提取

`./extract`目录中的脚本负责从emulator和FPGA的log中提取数据。
Emulator和FPGA的traffic log格式相同，都是
r'Traffic time: +(\d+) dsid: (\d) traffic: +(\d+)'。
其中Traffic time就是traffic对应的cycle数。

### 函数说明
`extract_emu_traffic.py`中的函数说明：

`get_emu_traffic_raw`基本上没什么用，提供的它的主要目的是log文件太大时，
在内存放不下可以支持迭代式的访问，然而log一般都很小，内存放得下。。

`get_emu_log`的两个参数是文件名和origin，origin的意思是是否将traffic中心化
（即让traffic从0开始、过原点）。
它的返回值是dict of lists of tuples，tuple就是(cycle, traffic)。
因为有很多个周期，所以需要list of tuples。
又因为有很多个DSID，所以需要dict of lists of tuples，dict的key就是DSID，
value则是该DSID产生的traffic log。

注意虽然上面两个函数名都带"emu"，但是实际上FPGA和emu的log格式相同，
所以他们对二者的log都适用。

`get_range_traffic`的基本功能和`get_emu_log`相似，主要增加了参数`start`和`end`。
它即只截取一段时间的log返回，这个功能可以用于画图和算带宽的时候选取范围。

`extract_bw.py`中的函数说明

`cal_bw`的输入包括log文件、range和dsid。
它干的事情就是给定log文件，算出指定周期区间内的带宽。
其中dsid可以不给，不给就算总带宽，给了就算全局带宽。
该脚本下面有调用该函数的例子。

## 画图

`./draw-linux-boot-cdf.py`这个脚本主要用于画emulator上Linux启动的流量cdf。
`./draw-spec.py`主要用于画FPGA上的cdf，下面主要介绍它的使用。

先下载 10.30.6.130:8000/example.log，
然后执行`python3 ./draw-spec.py example.log`，就会弹出matplot画的图。
在图里移动鼠标，右下角会显示鼠标对应的坐标，这样就可以找到自己关注的那一段的流量的范围。
比如绿色线上升的区间是1.3e10到1.39e11。
这个范围就可以用于计算带宽。

## 计算带宽

`cal-bw.py`用于计算带宽，使用方法：
`python3 ./cal-bw.py ./example.log -r 1.3e10 1.39e11`，
其中`1.3e10`和`1.39e11`就是我们选择的范围，可以用上面说的方法获取。
如果我们想得到特定的DSID的带宽，再加一个参数`-d`：
`python3 ./cal-bw.py ./example.log -r 1.3e10 1.39e11 -d 2`。
我们就可以得到绿色线对应的DSID在该范围内的带宽(7.46)。
