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
    response = requests.request("GET", url, headers=headers, params=querystring)
    return(response.text)

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        results = lookup(term=title, country=country)
        return render_template('results.html', results=results)
    else:
        return render_template('home.html')





if __name__ == "__main__":
    app.run(debug=True)