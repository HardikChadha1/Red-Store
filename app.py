from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

# Define an Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    cart_items = db.Column(db.String(500), nullable=False)  # Store cart items as JSON string

# Create the database tables
with app.app_context():
    db.create_all()

from flask import jsonify

@app.route('/submit-order', methods=['POST'])
def submit_order():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']
    cart_items = request.form['cart_items']  # Assume this is a JSON string of items

    # Create a new order instance
    new_order = Order(name=name, email=email, address=address, phone=phone, cart_items=cart_items)

    # Add to database
    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"status": "success", "message": "Order received!"})
    except:
        return jsonify({"status": "error", "message": "There was an issue processing your order."})
