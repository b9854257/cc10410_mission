
# coding: utf-8

# In[ ]:


撰寫一個Flask Server， 設計一個端口為user，用戶能對此端口用get方法訪問，傳回

    {"userId":1,"userName":"xiaoming"}


# In[1]:


"""
get 時 回傳json
"""
#引用flask套件
from flask import Flask, request, abort, jsonify
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )

#APP的訪問路徑
@app.route('/user',methods=['GET'])
def hello_world():
    t = {'userId':1,'userName':'xiaoming'}
    #回傳json格式
    return jsonify(t)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

