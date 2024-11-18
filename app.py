from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')




from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://negiseema621:Seema%4024@shop-db.j4ylx.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
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
