import os
import matplotlib.pyplot as plt

#设置中文字体（防止绘图时中文乱码，Windows通用）
plt.rcParams['font.sans-serif']=['SimHei']

def get_folder_size(folder_path):
    """计算一个文件夹的总大小"""
    total_size=0
    try:
        #os.walk返回 路径、文件夹名列表、文件名列表（递归的“深度搜索”）
        for dirpath,dirnames,filenames in os.walk(folder_path):
            for f in filenames:
                fp=os.path.join(dirpath,f)
                #累加每个文件的大小
                if os.path.exists(fp):
                    total_size+=os.path.getsize(fp)
                    #getsize返回的是字节，1KB=1024Byte，1MB=1024Byte
    except Exception as e:
        print(f"读取{folder_path}出错：{e}")
    return total_size/(1024*1024) #换算成MB


def analyze_disk_usage(target_dir):
    folder_names=[]
    folder_sizes=[]

    #获取目标目录下所有的子文件夹
    print("正在扫描，请稍后...")
    items=os.listdir(target_dir) #返回目标文件夹包含的文件（夹）名字列表，只能看到第一层文件（夹）
    for item in items:
        item_path=os.path.join(target_dir,item)
        if os.path.isdir(item_path):
            #计算每个子文件夹的大小
            size=get_folder_size(item_path)
            if size>0.1: #只记录大于0.1MB的文件夹，防止图表太乱
                folder_names.append(item)
                folder_sizes.append(size)

    #数据可视-画饼图
    if not folder_sizes:
        print("没有足够大的文件夹")
        return

    print("扫描完成，准备绘图...")
    plt.figure(figsize=(10,7)) #设置画布大小
    plt.pie(folder_sizes,labels=folder_names,autopct='%1.1f%%',startangle=140)
    plt.title(f"文件夹空间占用分析：{target_dir}")
    plt.axis('equal') #保证饼图是圆的
    plt.show()


analyze_disk_usage("D:/PythonProjects/_my_project")


