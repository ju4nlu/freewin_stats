from flask import Flask, escape, request, render_template
from freewin_stats.stats import get_player_details

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/player/')
@app.route('/player/<string:username>')
def show_user_profile(username: str = None):
    #return get_player_details(username)
    return render_template('hello.html', 
                           details=get_player_details(username))

@app.route('/match/')
@app.route('/match/<uuid:post_id>')
def show_post(post_id: str = None):
    return f'Match {post_id}'