from flask import Flask, render_template, request, redirect
from game_of_life import GameOfLife


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    height = ''
    width = ''
    if request.method == 'POST':
        height = request.form.get('height')
        width = request.form.get('width')
        #print(height)
        #print(width)
        GameOfLife(int(height), int(width))
        return redirect("/live")
    else:
        GameOfLife(20,20)
    return render_template('index.html', height=height, width=width)

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


