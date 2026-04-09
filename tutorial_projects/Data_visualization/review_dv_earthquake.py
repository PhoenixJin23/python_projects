import requests
import plotly.express as px
import pandas
from pandas import DataFrame


def plot_global_earthquakes():
    url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    response=requests.get(url)
    data=response.json()

    dicts=data['features']

    mags,titles,lons,lats=[],[],[],[]

    for d in dicts:
        mags.append(d['properties']['mag'])
        titles.append(d['properties']['title'])
        lons.append(d['geometry']['coordinates'][0])
        lats.append(d['geometry']['coordinates'][1])

    df=DataFrame({
        '震级':mags,
        '地点':titles,
        '经度':lons,
        '纬度':lats
    })

    fig=px.scatter_geo(df,lat='纬度',lon='经度',title="全球24小时地震分布图",
                       hover_name='地点',color='震级',projection="natural earth")
    fig.show()


plot_global_earthquakes()