from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app = Flask(__name__)
count = 0


@app.route('/')
def index():
    global count
    count = 0
    GameOfLife()
    return render_template(
        'index.html',

    )


@app.route('/live')
def live():
    global count
    GameOfLife(width=18, height=18)
    if count > 0:
        GameOfLife().form_new_generation()
    count = count + 1
    GameOfLife().counter = count


    return render_template(
        'live.html',
        life=GameOfLife()

    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
