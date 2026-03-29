import pandas as pd
import os


# 诊断微信账单
def diagnose_wechat(file_path):
    # 先只读前 20 行，不跳行，看看数据从哪开始
    df = pd.read_csv(file_path, encoding="utf-8", nrows=20)
    print("--- 微信账单前 20 行内容 ---")
    for i, row in df.iterrows():
        print(f"行号 {i}: {list(row.values)}")

# 运行诊断
#diagnose_wechat("C:/Users/g3472/Desktop/wechat.csv")


def clean_wechat_bill(file_path):
    #跳过微信账单前16行的说明
    #encoding='gbk'处理中文CSV
    try:
        # 兼容所有微信CSV编码
        df = pd.read_csv(file_path, skiprows=17, encoding="utf-8")
    except:
        df = pd.read_csv(file_path, skiprows=17, encoding="gb18030")

    #只保留需要的列，并重命名为统一格式
    #微信原始列名：交易时间, 交易类型, 交易对方, 商品, 收/支, 金额(元)
    df=df[['交易时间','商品','收/支','金额(元)','交易对方']]
    df.columns=['日期','商品','类型','金额','对方']

    #去掉金额前面的“¥”符号，并转为数字
    df['金额']=df['金额'].str.replace('¥','').astype(float)

    #只保留“支出部分”
    df=df[df['类型']=='支出']
    df['来源']='微信'
    return df


def clean_alipay_bill(file_path):
    #跳过前面24行说明
    try:
        # 兼容所有微信CSV编码
        df = pd.read_csv(file_path, skiprows=24, encoding="utf-8")
    except:
        df = pd.read_csv(file_path, skiprows=24, encoding="gb18030")

    #支付宝原始列名：交易时间, 商品说明, 收/支, 金额, 交易对方
    #支付宝列名后空格用strip()去掉
    df.columns=[c.strip() for c in df.columns]

    df=df[['交易时间','商品说明','收/支','金额','交易对方']]
    df.columns=['日期','商品','类型','金额','对方']

    # 支付宝金额已经是数字，只需过滤支出
    df=df[df['类型']=='支出']
    df['来源']='支付宝'
    return df


def merge_bills(wechat_csv,alipay_csv):
    print("正在处理账单...")

    #处理两个账单
    wechat_df=clean_wechat_bill(wechat_csv)
    alipay_df=clean_alipay_bill(alipay_csv)

    #合并
    combined_df=pd.concat([wechat_df,alipay_df],ignore_index=True)

    #按日期排序
    combined_df['日期']=pd.to_datetime(combined_df['日期'],format='mixed',errors='coerce')
    combined_df=combined_df.sort_values(by='日期')

    #保存为统一的CSV
    combined_df.to_csv("march_total_bill.csv",index=False,encoding='utf-8-sig')
    print(f"合并完成！共{len(combined_df)}笔支出，已保存为march_total_bill.csv")


#clean_wechat_bill("C:/Users/g3472/Desktop/wechat.csv")
#clean_alipay_bill("C:/Users/g3472/Desktop/alipay.csv")
merge_bills("C:/Users/g3472/Desktop/wechat.csv", "C:/Users/g3472/Desktop/alipay.csv")