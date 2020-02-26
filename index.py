from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "SELAMAT SIANG!"

@app.route("/setting")
def setting():
	return "Anda Berada Di Halaman Setting!!"

@app.route('/profil/<username>')
def show_profil(username):
	return "Anda Berada Di Halaman Profil %s" % username

if __name__ == "__main__":
    app.run()