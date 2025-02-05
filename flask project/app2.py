from flask import Flask, request,jsonify
app = Flask(__name__)
menu = [
    {'id': 1, 'name': 'idly', 'price': 40},
    {'id': 2, 'name': 'dosa', 'price': 60},
    {'id': 3, 'name': 'poori', 'price': 80}]
@app.route('/data',methods=['GET'])
def Hotel():
    return menu
@app.route('/add',methods=['POST'])
def add_item():
    
        data=request.json
        if not data:
                return jsonify({"error":"no data provided"}),400
        menu.append(data)     
        return jsonify({"message": "data added successfully","data": menu}) 
