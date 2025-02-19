
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample menu items (you can extend it with more items)
menu = {
    "breakfast": ["idly", "poori", "masal dosa"],
    "lunch": ["full meals", "Mutton Briyani", "chicken briyani"],
    "dinner": ["parotta", "idiyappam", "chapthi"],
    "dessert": ["halwa", "rasagulla", "gulab jamun"]
}
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()  
    

    selected_items = data.get('items', [])
    
    if not selected_items:
        return jsonify({"status": "error", "message": "No items selected"}), 400

    response = {
        "status": "success",
        "message": "Your order has been placed successfully!",
        "selected_items": selected_items
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)