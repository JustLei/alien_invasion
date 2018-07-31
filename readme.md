一个简单的2D游戏:**外星人入侵**

在运行之前需要在电脑中安装Pygame

相应的pygame文件已经在仓库中,我的电脑是windows64位,如果是不同类型的,可以到www.lfd.uci.edu/~gohlke/pythonlibs/#pygame进行下载

只需要打开命令窗口,切换到该文件所在的文件夹,并且用pip来运行它:

```
>python -m pip install --user pygame-1.9.4-cp36-cp36m-win_amd64.whl
#后面的文件名依据你下载的文件名而定
```

游戏说明:

- 飞船可上下左右移动,空格键发射子弹
- 初始生命值为3,不论是撞到外星人还是外星人到达屏幕底端,都将损失一条生命值
- 按p或者鼠标单击可开始游戏,按q可退出游戏
- 最高分储存在high_score中,此外,游戏中的一些参数设置在文件settings.py中
