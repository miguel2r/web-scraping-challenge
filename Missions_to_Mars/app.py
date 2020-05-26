from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars
#import pymongo


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsinfo_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
  
    mars_news = mongo.db.mars_news.find_one()
 
    # Return template and data
    return render_template("index.html", mars_d=mars_news)
  


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_newst = scrape_mars.scrape()
   
    # Update the Mongo database using update and upsert=True
    mongo.db.mars_news.update({}, mars_newst, upsert=True)
   

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)