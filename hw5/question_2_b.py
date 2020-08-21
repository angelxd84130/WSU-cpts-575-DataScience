from newsapi import NewsApiClient
import numpy as np
data = np.array([])
Alldata = []
def getPlan(data):
    Alldata = []
    for i in range(len(data)):
        del data[i]["source"]
        del data[i]["author"]
        del data[i]["description"]
        del data[i]["title"]
        del data[i]["url"]
        del data[i]["urlToImage"]
        del data[i]["publishedAt"]

        Alldata.append(data[i])
    return np.array(Alldata)

newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]

for i in range(len(Alltop)):
    data = np.array([])
    data = newsapi.get_top_headlines(category=Alltop[i], language='en', country='us', page_size=100).get('articles')
    #data = top_headlines.get('articles')
    print(data)
    Alldata.append(getPlan(data))
#print(data)
print(Alltop[1])#general
print(Alldata[1][2]["content"])# the thired article in general
print(type(data))
