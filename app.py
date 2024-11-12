from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/submit-order', methods=['POST'])
def submit_order():
    # Retrieve JSON data from the frontend
    order_data = request.json

    # Print order data to console for testing
    print("Order received:", order_data)

    # Send a response back to the frontend
    return jsonify({"status": "success", "message": "Order received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
