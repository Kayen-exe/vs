from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Are you a robot? You know where to go..."

@app.route("/robots.txt")
def robots():
    with open("robots.txt") as f:
        text = f.read()
    return text.replace("\n", "<br>")

@app.route("/goaway")
def go_away():
    return ("Ciphertext: 00011101 00011100 00010111 00000000 00001110 00010100 00000000 00011111 00011000 00000000<br>"+
            "Key: 01110000 01111001 01110100 01101000 01101111 01101110 01101001 01110011 01110100 01100001")

@app.route("/mechazilla")
def mechazilla():
    with open("mechazilla.html") as f:
        text = f.read()
    return text

@app.route("/42")
def universe():
    response = Response("Look into the Dev Tools for this one...")
    response.headers["try-visit"] =  "/iwashere"
    return response

@app.route("/sleep")
def sleep():
    response = Response("A: 10100101 10111100 01100110 10011011 11100001<br>" 
                        + "B: 00110010 01010000 00000001 00110110 01110001")
    response.headers["Operation"] = "Subtract"
    return response

@app.route("/iwashere")
def iwashere():
    response = Response("R2Igb3IgbmpueHIgdmYgZ2Igb3Igbnl2aXI=")
    response.headers["Operation"] =  "ROT-13"
    return response
    
@app.route("/henry")
def henry():
    with open("henry.html") as f:
        text = f.read()
    return text

@app.route("/cold")
def cold():
    return "https://pastebin.com/69F9niDw"

@app.route("/gopher")
def gopher():
    with open("gopher.html") as f:
        text = f.read()
    return text

@app.route("/pain")
def pain():
    with open("pain.html") as f:
        text = f.read()
    return text