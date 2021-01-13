print("""Hi Dr. 

Please Wait. Don't Quit. We will take care of every little things.


SANDIPAN LEFT SOME MESSEGE FOR YOU:
Hello, How are you? Hope you are in good Health...


""")
x=input("Press Enter to continue...")
from flask import Flask, request, render_template, Markup, url_for
import json, webbrowser
lisAlpha=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in lisAlpha:
	with open("data\\D"+i+".json") as f:
		globals()["D"+i] = json.load(f)

def dic_parser(word):
	word = word.upper()
	if word == "":
		return None
	X = word[0]
	if X in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		dic = globals()["D"+X]
		if word in dic.keys():
			total_res = dic[word]
			MEANINGS = list(total_res["MEANINGS"].values())
			ANTONYMS = total_res["ANTONYMS"]
			SYNONYMS = total_res["SYNONYMS"]
			return[MEANINGS, ANTONYMS, SYNONYMS]
		else:
			return None
	else:
		return None

app = Flask(__name__)

@app.route('/',methods = ["get","post"])
def index():
	if request.method == "POST":
		word = request.form.get('word')
		search_res = dic_parser(word)
		if search_res != None:
			MEANINGS = search_res[0]
			ANTONYMS = search_res[1]
			SYNONYMS = search_res[2]
		else:
			MEANINGS = [["Not Found.","",[],[]]]
			ANTONYMS = ["Not Found."]
			SYNONYMS = ["Not Found."]
	else:
		MEANINGS = [["Sandipan: Noun","Developer of this App.",[],[]],["Dr. P Pal: Noun","This app is made for him with heart.",[],[]]]
		ANTONYMS = []
		SYNONYMS = []

	return render_template('index.html',MEANINGS = MEANINGS, ANTONYMS = ANTONYMS, SYNONYMS = SYNONYMS)

if __name__ == '__main__':
	webbrowser.open('http://localhost:5000')
	app.run()