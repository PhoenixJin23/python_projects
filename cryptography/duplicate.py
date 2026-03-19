#Step1 用MD5获取文件的“指纹”
import hashlib
import os

def get_file_hash(file_path):
        #创建一个MD5探测器
        hasher=hashlib.md5()

        #以二进制读取模式打开文件('rb')，因为图片视频不是纯文本，必须读二进制
        with open(file_path,'rb') as f:
            #分块读取，防止文件太大破坏内存，一次读4096个字节
            chunk=f.read(4096)
            while len(chunk)>0:
                hasher.update(chunk) #把这块文件给探测器
                chunk=f.read(4096) #继续读下一块文件

        #返回最终生成的指纹（16进制字符串）
        return hasher.hexdigest()

    #print(get_file_hash("C:/Users/g3472/Desktop/cutiemice/others/0.dat"))


def find_duplicates(target_dir):
        #准备一个字典：{指纹：第一个发现文件的路径}：
        seen_hashes={} #{file_hash:
        #准备一个列表：记录所有发现的“twins”
        duplicates=[]

        files=os.listdir(target_dir)

        for filename in files: #filename是当前正在遍历的文件名
            file_path=os.path.join(target_dir,filename)

            if os.path.isfile(file_path):
                #计算当前文件的指纹
                file_hash=get_file_hash(file_path)

                #判断指纹是否重复
                if file_hash in seen_hashes:
                    original_file=seen_hashes[file_hash] #由指纹找到对应文件（第一个内容相同的文件）
                    print(f"发现重复！\n原件：{original_file}\n副本：{filename}\n")
                    duplicates.append(file_path)
                else:
                    #没见过，将它存进字典，作为“原件”来参考
                    seen_hashes[file_hash]=filename #seen_hashes={file_hash:filename}

        print(seen_hashes)
        print(duplicates)


        #询问用户是否要删除重复的
        if duplicates:
            confirm=input(f"共发现{len(duplicates)}个重复文件，输入'y'全部删除：")
            if confirm.lower()=='y':
                for dup_path in duplicates:
                    os.remove(dup_path)
                print("清理完毕！")
        else:
            print("文件夹很干净，没有重复的文件。")


find_duplicates("C:/Users/g3472/Desktop/cutiemice")






