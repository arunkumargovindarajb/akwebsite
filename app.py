from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/tos')
def tos():
    return render_template('tos.html')

@app.route('/app-ads.txt')
def app_ads():
    return send_from_directory('static', 'app-ads.txt')

if __name__ == "__main__":
    app.run()

##### AK Website 
