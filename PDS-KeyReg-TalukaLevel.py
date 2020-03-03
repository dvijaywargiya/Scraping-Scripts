#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import requests
from bs4 import BeautifulSoup as bs
import tqdm


# In[2]:


officeCodes = [1505180, 
          1505179,
          1505185,
          1505183,
          1505186,
          1505190,
          1505189,
          1505182,
          1505160,
          1505184,
          1505191,
          1505188,
          1505187,
          1506192,
          1506199,
          1506198,
          1506193,
          1506196,
          1506197,
          1506195,
          1509267,
          1509268,
          1509269,
          1509270,
          1509282,
          1509271,
          1509272,
          1509273,
          1509274,
          1509275,
          1509276,
          1509277,
          1509278,
          1509279,
          1509280,
          1509281,
          1508204,
          1508200,
          1508208,
          1508210,
          1508203,
          1508211,
          1508205,
          1508209,
          1508202,
          1508201,
          1508212,
          1508206,
          1507358,
          1507360,
          1507362,
          1507365,
          1507367,
          1507368,
          1507369,
          1507370,
          1504004,
          1504002,
          1504005,
          1504007,
          1504006,
          1504008,
          1504003,
          1504001]


# In[3]:


distCodes = []
for code in officeCodes:
    distCodes.append(int(str(code)[:4]))
distCodes


# In[10]:


url = "http://mahaepos.gov.in/fps_keyreg_cards.action?dist_code={0}&office_code={1}&month={2}&year={3}&status={4}"

mypayload = {}
myheaders = {

}

# HEADERS IN THE CSV TO BE ADDED MANUALLY

for t in range(12):
    month = t+1
    # CHANGE YEAR IN THE NEXT LINE
    temp = "TalukaLevel2018-{0}.csv"
    with open(temp.format(month), 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for ind in tqdm.tqdm(range(len(distCodes))):
            # CHANGE YEAR IN THE NEXT LINE
            temp = url.format(str(distCodes[ind]), str(officeCodes[ind]), str(month), str(2018), str(0))
            response = requests.request("GET", temp, headers=myheaders, data = mypayload)
            soup = bs(response.text, "lxml")
            tab = soup.findAll('table')
            if len(tab) == 0:
                continue
            rows = tab[0].findAll('tr')
            for ind in range(len(rows)):
                if ind >= 4 and ind < len(rows)-2:
                    data = []
                    tds = rows[ind].findAll('td')
                    if len(tds) == 0:
                        continue
                    fpsId = tds[1].findAll('a')[0].text
                    fpsId = fpsId.strip('\r\n ')
                    num = 0
                    for td in tds:
                        num = num + 1
                        if num == 1:
                            continue;
                        data.append(td.text)
                    data[0] = fpsId
                    csvwriter.writerow(data)


# In[ ]:




