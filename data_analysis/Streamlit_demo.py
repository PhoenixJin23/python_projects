import streamlit as st
import pandas as pd


st.title("简易账单分析器")

#上传文件
uploaded_file=st.file_uploader("上传你的账单CSV",type="csv")

if uploaded_file:
    #读取数据
    df=pd.read_csv(uploaded_file)

    #基础清洗（只保留日期和金额）
    df['日期']=pd.to_datetime(df['日期'])
    df['金额']=pd.to_numeric(df['金额'],errors='coerce')
    df=df.dropna(subset=['金额'])

    #展示核心指标
    total=df['金额'].sum()
    st.metric("总支出金额",f"￥{total:.2f}")

    #绘制趋势图
    st.subheader("每日支出趋势")
    daily_spending=df.groupby('日期')['金额'].sum()
    st.line_chart(daily_spending)

    #绘制分布图
    st.subheader("消费分布")
    #简化成按“对方”统计前十名
    top_tens=df.groupby('对方')['金额'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_tens)

    #显示原始数据表格
    st.subheader("账单明细")
    st.dataframe(df)