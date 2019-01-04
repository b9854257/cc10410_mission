
# coding: utf-8

# In[ ]:



描述

使用python的request模組去訪問`https://jsonplaceholder.typicode.com/users` 
取得第2,3,4,5 筆資料，

偵測當時日期，轉作檔名，將2345筆資料內容寫入檔案中。


# In[2]:


"""
Http Method - get


"""
#引用import套件
import requests
#擷取該網址內容
responseFromRemote = requests.get('https://jsonplaceholder.typicode.com/users')

# 有時我們想看response的body內容
#print(responseFromRemote.text)

# 若已經能預期傳回的內容為json格式，則可以直接將其轉為python可操作的資料格式
#print(responseFromRemote.json())

#回傳值轉json格式，並指定為a
a = responseFromRemote.json()

#引用datetime
import datetime
nowTime = datetime.datetime.utcnow().strftime("%Y-%m-%d")

#引用套件
import os
import shutil

#開啟檔案，以目前日期做檔名
abc = open(nowTime+'.txt','w')
abc.write(str(a[2]))
abc.write(str(a[3]))
abc.write(str(a[4]))
abc.write(str(a[5]))
# 將檔案關閉
abc.close()

