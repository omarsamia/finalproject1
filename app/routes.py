from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("Other_index.html")

@app.route('/results' , methods = ["GET", "POST"])
def results():
    if request.method == "GET":
        return render_template("Other_index.html")
    elif request.method == "POST":
        user_genre_dict = request.form
        print(user_genre_dict)
        user_genre = user_genre_dict["Genres"]
        song = model.song_picker(user_genre)
        print(song)
        return render_template('result3.html', user_genre = user_genre, song = song)    
    
        
    # elif request.method == "POST":
    #     user_data = request.form
    #     print(user_data)
    #     rap = user_data["Rap"]
    #     other = "Go back and fill out the form again"
    #     return render_template('results2.html', other = other)
        
