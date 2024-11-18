from dotenv import load_dotenv
import os
from flask import Flask, render_template
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# Ensure that both variables are set
if not MONGODB_USERNAME or not MONGODB_PASSWORD:
    raise ValueError("MONGODB_USERNAME and MONGODB_PASSWORD must be set in the .env file")

app = Flask(__name__)

# Use the MongoDB connection string with environment variables
mongo_uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@shop-db.j4ylx.mongodb.net/?retryWrites=true&w=majority&appName=shop-db"
client = MongoClient(mongo_uri)
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_data = list(products_collection.find())
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)
