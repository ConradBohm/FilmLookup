from flask import Flask, render_template, request
import requests
app = Flask(__name__)

url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

headers = {
    'x-rapidapi-key': "x",
    'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
    }

def lookup(term, country):
    querystring = {"term":f"{term}","country":f"{country}"}

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return lookup(term=title, country=country)
    else:
        return render_template('home.html')
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #return(response.text)




if __name__ == "__main__":
    app.run(debug=True)