# app.py
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (use MONGODB_URI env var or placeholder for setup)
client = MongoClient(os.environ.get("MONGODB_URI", "placeholder"))
db = client.car_unlock_system
users_collection = db['users']

# Helper function to check if the user exists
def user_exists(user_id, car_id):
    user = users_collection.find_one({"user_id": user_id, "car_id": car_id})
    return user

# Endpoint to unlock the car
@app.route('/unlock', methods=['POST'])
def unlock_car():
    data = request.get_json(silent=True) or {}
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    
    if not user_id or not car_id:
        return jsonify({"message": "user_id and car_id are required."}), 400

    # Check if the user exists
    user = user_exists(user_id, car_id)
    
    if user:
        return jsonify({"message": "Car unlocked successfully!"}), 200
    return jsonify({"message": "User not found or not authorized."}), 403

# Endpoint to lock the car
@app.route('/lock', methods=['POST'])
def lock_car():
    data = request.get_json(silent=True) or {}
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    
    if not user_id or not car_id:
        return jsonify({"message": "user_id and car_id are required."}), 400

    # Check if the user exists
    user = user_exists(user_id, car_id)
    
    if user:
        return jsonify({"message": "Car locked successfully!"}), 200
    return jsonify({"message": "User not found or not authorized."}), 403

if __name__ == '__main__':
    app.run(debug=True)
