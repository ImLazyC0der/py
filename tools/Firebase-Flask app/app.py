from flask import Flask, request, render_template
import pyrebase

config = {
	"apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(config)

database = firebase.database()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def getAndPost():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
            # root = firebase root or child name
			database.child("root").push(name)
			root = database.child("todo").get()
			data = root.val()
			return render_template('index.html', d = data.values())

		elif request.form['submit'] == 'delete':
			database.child("root").remove()

		return render_template('index.html')

	return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)