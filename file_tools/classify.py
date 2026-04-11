import os

#task:扫描一个文件夹，根据文件的后缀名（如.jpg,.pdf,.py），自动把它们移动到对应的子文件夹里。

def classify_files(target_dir):
    #定义分类规则
    extension_rules={
        ".png":"images",
        ".jpg":"images",
        ".jpeg":"images",
        ".heic":"images",
        ".pdf":"documents",
        ".docx":"documents",
        ".txt":"documents",
        ".py":"python_scripts",
        ".zip":"archives"
    }

    #从目标文件夹中获取所有文件
    files=os.listdir(target_dir)

    for filename in files:
        #构造文件的完整路径（文件夹+文件名）
        old_path=os.path.join(target_dir,filename)

        #过滤文件夹，只处理文件
        if os.path.isfile(old_path):
            #获取文件后缀名：os.path.splitext
            _,extension=os.path.splitext(filename)
            extension=extension.lower() #后缀名全部转化为小写

            if extension in extension_rules:
                folder_name=extension_rules[extension] #由后缀名对应文件类型
            else: #不在规则里，就去others
                folder_name="others"

            folder_path=os.path.join(target_dir,folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"创建了新文件夹{folder_name}")

            #移动文件进行重新分类
            new_path=os.path.join(folder_path,filename)

            if not os.path.exists(new_path):
                os.rename(old_path,new_path)
                print(f"已分类{filename}--->{folder_name}")
            else: #如果目标位置已经有同名文件了，先不移动，防止覆盖
                print(f"跳过: {filename} (目标文件夹已存在同名文件)")


classify_files("C:/Users/g3472/Desktop/cutiemice")




