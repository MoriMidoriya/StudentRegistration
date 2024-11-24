from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Adjust host if needed
    db = client["student_registration"]
    collection = db["students"]
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)

@app.route("/")
def page():
    return render_template("page.html")  # Serve the frontend page

@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()  # Fetch JSON data from the request
        print("Received data:", data)

        # Insert the document into MongoDB
        student = {
            "name": data["name"],
            "reg_number": data["reg_number"],
            "email": data["email"],
            "mobile": data["mobile"],
            "location": data["location"],
        }
        result = collection.insert_one(student)
        print(f"Inserted student with ID: {result.inserted_id}")

        return jsonify({"message": "Student registered successfully!"}), 200
    except Exception as e:
        print("Error during insertion:", str(e))
        return jsonify({"error": str(e)}), 500

# Route to fetch all registered students
@app.route("/students", methods=["GET"])
def get_students():
    try:
        students = list(collection.find())  # Fetch all students
        for student in students:
            student["_id"] = str(student["_id"])  # Convert ObjectId to string for JSON compatibility
        return jsonify({"students": students}), 200
    except Exception as e:
        print("Error fetching students:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
