from flask import Flask

app= Flask(__name__)
@app.route("/")
def hello():
	return "Hello World!"
	
@app.route("/a")
def hllo():
	return " World!"
	

	
#app.run(debug=True)
app.run()