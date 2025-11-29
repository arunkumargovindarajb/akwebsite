from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Home page
@app.route("/")
def base():
    return render_template("base.html")

# 2048 subpage
@app.route('/about_2048')
def about_2048():
    return render_template('about_2048.html')

# Other pages
@app.route('/how_to_play_2048')
def how_to_play_2048():
    return render_template('how_to_play_2048.html')

# Other pages
@app.route('/privacy_policy_2048')
def privacy_policy_2048():
    return render_template('privacy_policy_2048.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/tos')
def tos():
    return render_template('tos.html')

# Serve static app-ads.txt
@app.route('/app-ads.txt')
def app_ads():
    return send_from_directory('static', 'app-ads.txt')

if __name__ == "__main__":
    app.run(debug=True)

##### AK Website