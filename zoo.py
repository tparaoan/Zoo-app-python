from flask import Flask, request, Response
import json

app = Flask (__name__)
#KEY : VALUE
animal_db = {
    "1": {"name": "Zebra", "origin": "Africa"},
    "2": {"name": "Panda", "origin": "China"},
    "3": {"name": "Kangaroo", "origin": "Australia"}
}

@app.route("/")
def index():
    return "Welcome to the Zoo!"

@app.route("/animals")
def list_animals():
    return animal_db


@app.route("/animal/ <animal_id>")
def get_animal(animal_id):
    return animal_db[animal_id]

@app.route("/animal/add", methods= ['POST'])
def add_animal ():
    req_data = request.get_json()
    new_animal = req_data["animal"]
    new_id = len(animal_db) + 1
    new_animal_data = { str(new_id) : new_animal }
    animal_db.update(new_animal_data)
    return "The animal was added successcully"

@app.route("/animal/update", methods= ['POST'])
def update_animal():
    req_data = request.get_json()
    animal_db.update (req_data)
    return "The animal is updated"
    

    
    
if __name__ == "__main__":
    app.run(host = "127.0.0.1")
        