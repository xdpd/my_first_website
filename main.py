from flask import Flask, render_template, request
import requests

site = Flask(__name__)

def get_fact(theme, lang):
    try:
        if theme == "general":
            r = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
            fact = r.json()["text"]

        elif theme == "cat":
            r = requests.get("https://catfact.ninja/fact")
            fact = r.json()["fact"]

        elif theme == "dog":
            r = requests.get("https://dogapi.dog/api/v2/facts")
            fact = r.json()["data"][0]["attributes"]["body"]
            
        else:
            fact = "No fact"

        if lang == "ua":
            tr = requests.get(f"https://api.mymemory.translated.net/get?q={fact}&langpair=en|uk")
            fact = tr.json()["responseData"]["translatedText"]

        return fact
    
    except:
        return "Error"

@site.route("/")
def main_page():
    theme = request.args.get("theme", "general")
    mode = request.args.get("mode", "dark")
    lang = request.args.get("lang", "en")
    fact = get_fact(theme, lang)
    return render_template("index.html", fact=fact, theme=theme, mode=mode, lang=lang)

if __name__ == "__main__":
    site.run(debug=True)