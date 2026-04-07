import requests
import plotly.express as px


url="https://api.github.com/search/repositories"
url+="?q=topic:deep-learning+language:python+sort:stars+stars:>10000"

headers={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url,headers=headers)

print(f"状态码为：{r.status_code}")
response_dict=r.json()
print(response_dict.keys())
#print(response_dict['items'])
repo_dicts=response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

#count=1
hover_texts,stars,repo_links=[],[],[]
for repo in repo_dicts:
    #print(f"第{count}个：")
    #print(f"Name:{repo['name']}")
    #print(f"}")
    #print(f"Url:{repo['html_url']}")Owner:{repo['owner']['login']
    #print(f"Description:{repo['description']}")
    #print(f"Date:{repo['created_at']}")
    #print(f"Stars:{repo['stargazers_count']}")
    #print("\n")
    #count+=1
    repo_name=repo['name']
    Url=repo['html_url'] #!这里提取出来的链接不会自带引号
    repo_link=f"<a href='{Url}'>{repo_name}</a>" #实现在点击repo_name的时候跳转到对应的url
    repo_links.append(repo_link)

    Owner=repo['owner']['login']
    Description=repo['description']
    hover_text=f"{Owner}<br />{Description}" #<br />标签起换行作用
    hover_texts.append(hover_text)
    Stars=repo['stargazers_count']
    stars.append(Stars)


title="Most Starred Deep Learning Projects On Github"
labels={'x':"project",'y':"stars"}
fig=px.bar(x=repo_links,y=stars,hover_name=hover_texts,title=title,labels=labels) #横、竖、悬浮区都必须为列表/数组/序列形式
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.show()
