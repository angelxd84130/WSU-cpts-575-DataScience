from newsapi import NewsApiClient
import numpy
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
    return Alldata

def replaceSystem(string):
    for char in string:
        if char in "~!@#$%^&*()[]{},+-|/?<>'.;:0123456789":
            string = string.replace(char, '')
    return string

def split_line(text):
    text = replaceSystem(text)
    text = text.lower()
    words = text.split()
    return words


newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
print("start download news:")
for i in range(len(Alltop)):
    top_headlines = newsapi.get_top_headlines(category=Alltop[i], language='en', country='us', page_size=100)
    data = top_headlines.get('articles')
    Alldata.append(getPlan(data))
    print("finish", i+1, "/6")

from collections import Counter
count = [[],[],[],[],[],[]]
#print(type(count[0]))
for i in range(6):
    count[i] = Counter()
#print(type(count[i]))

print("start get dic")
for i in range(len(Alldata)):
    for j in range(len(Alldata[i])):
        #print("ij", i, j)
        alist = Alldata[i][j]["content"]
        if alist!=None:
            alist = split_line(alist)
            for word in alist:
                count[i][word] += 1
    print("finish", i + 1, "/6")
    print(count[i])

