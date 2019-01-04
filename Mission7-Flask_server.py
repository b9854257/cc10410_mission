
# coding: utf-8

# In[1]:


撰寫一個Flask Server， 設計一個端口為user，用戶能對此端口用GET方法訪問，
並且挾帶query string，
id=xxx。 若用戶傳入 id=123，則傳回json


# In[ ]:


"""
flask get結合query string

使用時，查詢http://192.168.114.10:5000?userId=xxx

"""

from flask import Flask, request, abort, jsonify
app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/" )

@app.route('/',methods=['GET'])
def hello_world():
    t = request.args.get('userId')
    jsonDict = {'userId':t}
    return jsonify(jsonDict)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

