from flask import Flask, render_template, request
import requests #for sending request using api

app = Flask(__name__) #server start
app.config["DEBUG"]=True #debug mode on- no need to server restart

@app.route("/", methods=["GET", "POST"])    #routing/mapping
def home():                                 #function
    if request.method == "GET":             #taking get request input
        return render_template("index.html")#display html page (VIEW)

    elif request.method == "POST":          #taking post request - (abstraction)
        userInput = request.form.get("userInput") #fecthing input form index.html page

        link = "https://api.openweathermap.org/data/2.5/weather?APPID=2f6d0670b50ea9638ade4f6d1aae038d&units=metric&q=" + userInput
        #open_public_weather_api_key

        r = requests.get( link )    #getting data in json format after api request.
        r = r.json()                #converting json data to pyhton list.

        api_data = r["main"]        #extracting useful data
        api_data2 = r["coord"]

        return render_template("result.html", data = api_data) #passing data to html using jinja.
        
@app.route("/about")
def about():
    return render_template("about.html")


app.run(port=80) #http port - 80
