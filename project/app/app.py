from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_client = MongoClient("mongodb://mongodb:27017/")
db = mongo_client["test_database"]

# Routes
@app.route('/')
def index():
    return 'Welcome to the Python web app!'

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if db.users.find_one({"username": username, "password": password}):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/comment', methods=['POST'])
def comment():
    data = request.json
    comment = data.get('comment')
    db.comments.insert_one({"comment": comment})
    return jsonify({"message": "Comment added successfully"}), 200

@app.route('/email', methods=['POST'])
def email():
    data = request.json
    email = data.get('email')
    db.emails.insert_one({"email": email})
    return jsonify({"message": "Email submitted successfully"}), 200
@app.route('/projects')
def git_project_carousel(projects_info):
    """
    Function to rotate between Git projects, their corresponding URLs, and background images.

    Args:
    - projects_info (list of tuples): List of tuples where each tuple contains (project_directory, project_url, image_path).
                                      project_directory (str): The directory where the Git project is stored.
                                      project_url (str): The URL for viewing the project.
                                      image_path (str): The path to the background image for the project.

    Returns:
    - tuple: (project_path, project_url, image_path)
        - project_path (str): Path to the current Git project.
        - project_url (str): URL to view the current Git project.
        - image_path (str): Path to the background image for the current project.
    """

    if not projects_info:
        print("No projects provided.")
        return None, None, None

    # Read the last accessed project index
    index_file = '.carousel_index'
    current_index = 0
    if os.path.exists(index_file):
        with open(index_file, 'r') as f:
            current_index = int(f.read().strip())

    # Cycle through projects
    current_project_info = projects_info[current_index]
    current_index = (current_index + 1) % len(projects_info)

    # Save the current project index
    with open(index_file, 'w') as f:
        f.write(str(current_index))

    return current_project_info

# Example usage:
projects_info = [
    ("/path/to/project1", "http://project1url.com", "/path/to/image1.jpg"),
    ("/path/to/project2", "http://project2url.com", "/path/to/image2.jpg"),
    # Add more projects here as needed
]

current_project_path, current_project_url, current_image_path = git_project_carousel(projects_info)
print("Current Git project path:", current_project_path)
print("URL to view the current Git project:", current_project_url)
print("Background image path:", current_image_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
