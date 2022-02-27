from flask import Flask,render_template
app=Flask(__name__)

#name1=input("Name :")

@app.route("/")
def hello():
	name="Aaftab"
	return render_template("index.html",name=name)
	
app.run(debug=True)