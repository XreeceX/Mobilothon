# Car Unlock System

This project is a simple car unlocking and locking system using Flask and MongoDB. It allows users to lock and unlock their cars using a generated token.

---

## Features
- Add user-car associations with a unique token (`add_data.py`).
- Unlock a car using the `/unlock` API endpoint.
- Lock a car using the `/lock` API endpoint.
- MongoDB integration for secure storage of user and car data.

---

## Prerequisites
- Python 3.x installed
- MongoDB Atlas account (or a local MongoDB instance)
- Dependencies from `requirements.txt` (Flask and pymongo)

---

## Installation
1. **Clone the repository:**
  ```bash
  git clone https://github.com/XreeceX/Mobilothon
  cd Mobilothon
```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Mongodb**
  - Create a MongoDB Atlas cluster or install a local MongoDB instance.
  - Update the connection string in both add_data.py and app.py files.

4. **Run the Application**
   ```bash
   python app.py
   ```

## Usage
### add_data.py

 1. Run the script:
```bash
python add_data.py
```
 2. To unlock a car, send a POST request to `/unlock` with a JSON payload containing `user_id` and `car_id`.
 3. To lock a car, send a POST request to `/lock` with a JSON payload containing `user_id` and `car_id`.

The application will check the user's authorization based on the data stored in the MongoDB users collection.
