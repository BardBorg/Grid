# db.py
# from flask import Flask
# from flask_mysqldb import MySQL
import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# mysql = MySQL(app)
CORS(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Password'
# app.config['MYSQL_DB'] = 'flaska'
app.config['MYSQL_DB'] = 'forgrid'
mysql = pymysql.connect(
    host='localhost',
    user='root',
    password='Password',
    
    db = app.config['MYSQL_DB']
)
@app.route('/api/data', methods=['GET'])
def index():
    
    cursor = mysql.cursor()

    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM dane''')
    # results = cur.fetchall()
    
    # cur.close()
    query = "SELECT * FROM dane"
    cursor.execute(query)
    results = cursor.fetchall()   
    mysql.commit()
    cursor.close() 
    
    newList=list(results)
    # print(newList)
    data_list = []
    for record in newList:
        record_dict = {
            'ID': record[0],
            'Name': record[1],
            'Email': record[2],
            'Role': record[3]
    }
        data_list.append(record_dict)
    # return results
    response_data={"results": data_list}
    # for x in range(6):
    jsonObject= jsonify({'ID': results[0][0],'Name':results[0][1],'Email':results[0][2], 'Role':results[0][3]})
    jsonObj=jsonify(response_data)
    # print(results)
    # return jsonify(data_list)
    return jsonObj
if __name__ == '__main__':
    app.run(debug=True)