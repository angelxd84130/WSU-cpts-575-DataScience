import numpy
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
top_headlines = newsapi.get_top_headlines(category='science', language='en',
                                          country='us', page_size=100)
#all_articles = newsapi.get_everything(sources='bbc-news')
#newsapi.get_everything()
#sources = newsapi.get_sources()
# print(len(all_articles['articles']), all_articles.keys(), all_articles['totalResults'])
data = top_headlines.get('articles')
for i in range(len(data)):
    print(i, ":", data[i])

print(len(data))
'''
from importguardian import importguardian

import json
import requests

from os import makedirs
from os.path import join, exists
from datetime import date, timedelta

ARTICLES_DIR = join('tempdata', 'articles')
makedirs(ARTICLES_DIR, exist_ok=True)
# Sample URL
#
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here

#MY_API_KEY = open("creds_guardian.txt").read().strip()
API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    'from-date': "",
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': 'efd9527d-bbfe-4481-9a7a-b8c2af6706ba'
}

start_date = date(2012, 3, 1)
end_date = date(2012,4, 30)
dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    fname = join(ARTICLES_DIR, datestr + '.json')
    if not exists(fname):
        # then let's download it
        print("Downloading", datestr)
        all_results = []
        my_params['from-date'] = datestr
        my_params['to-date'] = datestr
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            print("...page", current_page)
            my_params['page'] = current_page
            resp = requests.get(API_ENDPOINT, my_params)
            data = resp.json()
            all_results.extend(data['response']['results'])
            # if there is more than one page
            current_page += 1
            total_pages = data['response']['pages']

        with open(fname, 'w') as f:
            print("Writing to", fname)

            # re-serialize it for pretty indentation
            f.write(json.dumps(all_results, indent=2))
'''