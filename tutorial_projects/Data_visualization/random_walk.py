from random import choice #choice帮我们做随机决策


class RandomWalk:
    """一个生成随机游走数据的类"""

    def __init__(self,num_points=5000):
        """初始化随机游走的属性"""
        self.num_points=num_points #每次随机走的数量
        #所有随机游走都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]


    def fill_walk(self):
        """计算随机游走包含的所有点"""
        #不断游走，直到列表达到指定的长度
        while len(self.x_values)<self.num_points:
            #决定前进的方向以及沿这个方向前进的距离
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue #继续循环，刚刚生成的点不算

            #计算下一个点的x值和y值
            y=self.y_values[-1]+y_step #这次点的纵坐标值=上一个点的纵坐标值+纵向变化的值
            x=self.x_values[-1]+x_step #列表索引，-1代表列表的最后一个数值（在列表中依次添加到每一个都是最后一个）
            #取数组最后一个元素的简写方式等同于self.y_values[len(self.y_values) - 1]

            self.x_values.append(x)
            self.y_values.append(y)


