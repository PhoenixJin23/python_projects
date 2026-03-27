import pandas as pd
import matplotlib.pyplot as plt
from unicodedata import category

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


def auto_category(row):
    """这是一个简单的‘智能分类器’
    根据商品名或交易对方，自动返回类别"""
    item=str(row['商品'])+str(row['对方'])

    if any (keyword in item for keyword in [ '卓美','网盘','春暖花开','流量','懒耶耶','群红包','Lucky','洗衣液','浴帽','梳子','洗脸巾']):
        return '生活'
    elif any (keyword in item for keyword in [ '暨','咖','肉','超市','收','便利店','易站','叮叮咚','唐','敦','公','UNI']):
        return '吃'
    elif any (keyword in item for keyword in [ '通','出行','巴士','MTR','地铁','订单']):
        return '行'
    elif any (keyword in item for keyword in [ '烧女图','女子','猫眼','消费','SHOP']):
        return '书影音'
    elif any (keyword in item for keyword in [ '莉莉','Tory']):
        return '衣'
    else:
        return '其它'


def run_analysis(csv_path):
    #读取合并后的账单
    df=pd.read_csv(csv_path)
    df['日期']=pd.to_datetime(df['日期'])

    #应用自动分类逻辑，产生一个新列“类别”
    df['类别']=df.apply(auto_category,axis=1)

    #分析1：日消费趋势
    daily_spending=df.groupby(df['日期'].dt.date)['金额'].sum()

    #分析2：类别占比
    category_spending=df.groupby('类别')['金额'].sum()

    #绘图（包含两个子图的画布）
    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(12,10))
    plt.subplots_adjust(hspace=0.4) #调整子图间距

    #绘制折线图（日趋势）
    ax1.plot(daily_spending.index,daily_spending.values,marker='o',color='#ff7f0e',linewidth=2)
    ax1.set_title('一个月每日支出趋势',fontsize=14)
    ax1.set_ylabel('金额（元）')
    ax1.grid(True,alpha=0.3)

    #绘制饼图（类别占比）
    ax2.pie(category_spending.values,labels=category_spending.index,autopct='%1.1f%%',
             startangle=140,colors=['#1f77b4','#2ca02e','#d62728','#9467bd','#8c564b'])
    ax2.set_title('一个月消费结构占比',fontsize=14)

    #打印简单的文字总结
    print(f"---一个月账单简报---")
    print(f"总支出:{df['金额'].sum():.2f}元")
    print(f"单笔最高:{df['金额'].max():.2f}元({df.loc[df['金额'].idxmax(),'商品']})")
    print(f"最常消费的类别:{category_spending.idxmax()}")

    plt.show()


run_analysis("C:/Users/g3472/Desktop/march_total_bill.csv")


