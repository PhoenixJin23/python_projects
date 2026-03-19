import os #Python内置的操作系统交互的核心库，核心用于文件（夹）处理
import json #Python内置数据处理模块，用来储存键值对

def obfuscate_files(folder_path): #(文件夹的路径)
    # 将对应关系保存到JSON文件中（“钥匙”）
    key_path = os.path.join(folder_path, "key.json")
    if os.path.exists(key_path):
        print("错误：检测到钥匙文件已存在，说明文件夹可能已经处于混淆状态！请先还原再操作。")
        return

    #获取文件夹内所有文件名
    files=os.listdir(folder_path)

    #用于存储{新文件名：旧文件名}的字典
    name_map={}

    #钥匙文件的名字
    key_name="key.json"

    count=0

    #循环遍历文件夹里的所有文件/文件夹名称，同时给每个元素分配一个数字序号
    for old_name in files: #enumerate是Python内置函数，专门给遍历的元素加 “序号”
        if old_name==key_name:   #不用enumerate是因为它会预先分配序号，包括给key.json
            continue #跳过钥匙文件

        #构造旧文件的完整路径（文件夹路径+旧文件名）
        old_path=os.path.join(folder_path,old_name) #path.join是拼接路径的函数

        #确保它是一个文件而不是文件夹
        if os.path.isfile(old_path):
            #生成新名字，例如：secret_0.dat
            #使用手动计数器
            new_name=f"secret_{count}.dat"
            new_path=os.path.join(folder_path,new_name)

            #执行重命名
            os.rename(old_path,new_path)

            #记录对应关系
            name_map[new_name]=old_name #通过键（新名）找值（原名）是最快的 字典[键]=值

            count+=1

    with open(key_path,"w",encoding="utf-8") as f: #with可自动关闭文件，不用f.close()
        json.dump(name_map,f,ensure_ascii=False,indent=4)
        #dump把Python数据（字典/列表）写入JSON文件
        #ensure_ascii=False 关闭“强制用ASCII编码”,保证中文等非ASCII字符正常显示
        #indent=4 格式化缩进4格对齐
    print(f"混淆完成，共处理{count}个文件，钥匙已保存在{key_path}")


def restore_files(folder_path):
    #读取JSON钥匙文件
    key_path = os.path.join(folder_path, "key.json")
    #检查钥匙是否存在
    if not os.path.exists(key_path):
        print("找不到钥匙文件key.json！")
        return

    with open(key_path,"r",encoding="utf-8") as f:
        name_map=json.load(f)

    #遍历字典进行还原
    for secret_name,original_name in name_map.items():
        current_path=os.path.join(folder_path,secret_name)
        original_path=os.path.join(folder_path,original_name)

        #如果文件确实存在，就改回去
        if os.path.exists(current_path):
            os.rename(current_path,original_path)

    print("还原完成！")
    os.remove(key_path)

obfuscate_files(f"C:/Users/g3472/Desktop/cutiemice")
#restore_files(f"C:/Users/g3472/Desktop/cutiemice")
