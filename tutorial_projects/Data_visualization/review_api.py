import requests


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

count=1
for repo in repo_dicts:
    print(f"第{count}个：")
    print(f"Name:{repo['name']}")
    print(f"Owner:{repo['owner']['login']}")
    print(f"Url:{repo['html_url']}")
    print(f"Description:{repo['description']}")
    print(f"Date:{repo['created_at']}")
    print(f"Stars:{repo['stargazers_count']}")
    print("\n")
    count+=1
