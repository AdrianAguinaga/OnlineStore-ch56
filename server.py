from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World CH56!</p>"


@app.get("/test")
def test():
    return "This is a test endpoint 1.0."


@app.get("/home")
def home():
    print("Home endpoint accessed")
    return "Welcome to the home page!"


@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}


@app.get("/api/about")
def about():
    print("About endpoint accessed")
    name = {"name": "Leo Miranda"}
    return name


@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Jeffrey", "George", "Nar", "Rafael", "Isai", "Erick"]
    return student_names


@app.get("/greet/<name>")
def greet(name):
    print("Greet endpoint accessed")
    # return "Hello " + name
    return f"Hello {name}"


@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user_name = "Pam"
    age = 25
    return render_template("contact.html", name=user_name, age=age)

products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print(item)
    #mock save
    products.append(item)
    return json.dumps(item)

# PUT
@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item = request.get_json()
    if len(products) > index >= 0:
        products[index]= updated_item
        return json.dumps(updated_item)
    else:
        return "that index does not exist" 

# Try to use the delete method-- it uses the same logic but use pop instead
@app.delete("/api/products/<int:index>")
def delete_fuction(index):
    delete_item = request.get_json()
    if 0<= index < len(products):
        delete_item = products.pop(index)#This is the only line that you need to change the
        # logic to update the element
        return json.dumps(delete_item)
    else:
        return "that index does not exist"
# patch
@app.patch("/api/products/<int:index>")
def patch_fuction(index):
    patch_item = request.get_json()
    if 0<= index < len(products):
        # HERE is the challenge
        products(index).update(patch_item)
        return json.dumps(patch_item)
    else:
        return "that index does not exist"



# @app.post
# @app.put
# @app.delete
# @app.patch

app.run(debug=True, port=8000)
