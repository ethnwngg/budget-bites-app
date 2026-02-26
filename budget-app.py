from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://ethanwong_db_user:0rrmjHFQeamCG3cn@budget-db.tlbx63r.mongodb.net/?appName=budget-db"
client = MongoClient(MONGODB_URI)

db = client["budget-bites"]
collection = db["food"]

app = Flask(__name__)

data = [
    {
        "name" : "Chipotle",
         "price" : 12.99,
         "image_url" : "https://www.trophyclub.org/ImageRepository/Document?documentId=10395"
     },
     {
         "name" : "Starbucks",
         "price" : 5.99,
         "image_url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc04AHM_-3F1WLk3-DGTOu0FLT0FB8vKYYSQ&s"
     },
     {
         "name" : "Domino's Pizza",
         "price" : 8.99,
         "image_url" : "https://www.dominos.com/static/1.122.1/images/tiles/mixAndMatchDealPSC/hero.webp"
     },
     {
         "name" : "Dunkin' Donuts",
         "price" : 6.99,
         "image_url" : "https://s3.amazonaws.com/cms.ipressroom.com/285/files/20212/605496ebb3aed365bf70a284_Dunkin%27s+Commitment+to+Lessening+Food+Waste/Dunkin%27s+Commitment+to+Lessening+Food+Waste_73c232b5-d180-4d0c-a6f8-7751f17befb2-prv.jpg"
     },
     {
         "name" : "McDonald's",
         "price" : 7.99,
         "image_url" : "https://s7d1.scene7.com/is/image/mcdonalds/DC_202307_8936_EVM_M_BigMac_Coke_1564x1564-1:product-header-mobile?wid=1313&hei=1313&dpr=off"
     },
     {
         "name" : "CAVA",
         "price" : 12.99,
         "image_url" : "https://visithampton.com/wp-content/uploads/cava-800x800-with-logo.png"
     }
 ]

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>Welcome to CS4800! Enjoy the full-stack dev!</em></h1></body></html>"

@app.route("/search/<budget>")

def search_food_items(budget):
    budget = float(budget)
    result = []
    for food in collection.find():
        if food['price'] <= budget:
            food["_id"] = str(food["_id"])
            result.append(food)
    return result

app.run(host= "0.0.0.0", port=5005)