from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from config import Config
from game_of_life import *
from forms import Dimensions_world_Form

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    width = None
    height = None
    form = Dimensions_world_Form()
    if form.validate_on_submit():
        width = form.width.data
        height = form.height.data
        GameOfLife(width, height)
        print("\nData received. Now redirecting...")
        return redirect(url_for('index'))

    return render_template('index.html', form=form,
                           height = height,
                           width = width,
                           )

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter_generations > 0:
        game.form_new_generation()
    game.counter_generations += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)


