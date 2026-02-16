# app.py
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB: use MONGODB_URI or construct from MONGO_PASSWORD
_mongo_uri = os.environ.get("MONGODB_URI")
if not _mongo_uri:
    _password = os.environ.get("MONGO_PASSWORD", "")
    _mongo_uri = f"mongodb+srv://player:{_password}@cluster0.oe6qr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" if _password else "placeholder"
client = MongoClient(_mongo_uri)
db = client.car_unlock_system
users_collection = db['users']

# Helper function to check if the user exists
def user_exists(user_id, car_id,token):
    user = users_collection.find_one({"user_id": user_id, "car_id": car_id, "token": token})
    return user

# Endpoint to unlock the car
@app.route('/unlock', methods=['POST'])
def unlock_car():
    data = request.get_json(silent=True) or {}
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    token=data.get('token')
    
    if not user_id or not car_id or not token:
        return jsonify({"message": "user_id, car_id and token are required."}), 400

    # Check if the user exists
    user = user_exists(user_id, car_id, token)
    
    if user:
        return jsonify({"message": "Car unlocked successfully!"}), 200
    return jsonify({"message": "User not found or not authorized."}), 403

# Endpoint to lock the car
@app.route('/lock', methods=['POST'])
def lock_car():
    data = request.get_json(silent=True) or {}
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    token=data.get('token')
    
    if not user_id or not car_id or not token:
        return jsonify({"message": "user_id, car_id and token are required."}), 400

    # Check if the user exists
    user = user_exists(user_id, car_id, token)
    
    if user:
        return jsonify({"message": "Car locked successfully!"}), 200
    return jsonify({"message": "User not found or not authorized."}), 403

if __name__ == '__main__':
    app.run(debug=True)
