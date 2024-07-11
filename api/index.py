from flask import Flask, url_for, request, render_template, session
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return 'a href=\"{url_for("about")}\">About</a>'

@app.route('/about')
def about():
    return 'About'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

#~ @app.route('/path/<path:subpath>')
#~ def show_subpath(subpath):
    #~ # show the subpath after /path/
    #~ return f'Subpath {escape(subpath)}'

#~ @app.route('/login', methods=['POST', 'GET'])
#~ def login():
    #~ error = None
    #~ if request.method == 'POST':
        #~ if valid_login(request.form['username'],
                       #~ request.form['password']):
            #~ return log_the_user_in(request.form['username'])
        #~ else:
            #~ error = 'Invalid username/password'
    #~ # the code below is executed if the request method
    #~ # was GET or the credentials were invalid
    #~ return render_template('login.html', error=error)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#~ @app.get('/login')
#~ def login_get():
    #~ return show_the_login_form()

#~ @app.post('/login')
#~ def login_post():
    #~ return do_the_login()

#~ url_for('static', filename='style.css')
#~ searchword = request.args.get('key', '')
#~ username = request.cookies.get('username')
#~ resp.set_cookie('username', 'the username')
#~ return redirect(url_for('login'))
#~ abort(401)

#~ @app.route("/me")
#~ def me_api():
    #~ user = get_current_user()
    #~ return {
        #~ "username": user.username,
        #~ "theme": user.theme,
        #~ "image": url_for("user_image", filename=user.image),
    #~ }

#~ @app.route("/users")
#~ def users_api():
    #~ users = get_all_users()
    #~ return [user.to_json() for user in users]


#~ @app.route('/')
#~ def index():
    #~ if 'username' in session:
        #~ return f'Logged in as {session["username"]}'
    #~ return 'You are not logged in'

#~ @app.route('/login', methods=['GET', 'POST'])
#~ def login():
    #~ if request.method == 'POST':
        #~ session['username'] = request.form['username']
        #~ return redirect(url_for('index'))
    #~ return '''
        #~ <form method="post">
            #~ <p><input type=text name=username>
            #~ <p><input type=submit value=Login>
        #~ </form>
    #~ '''

#~ @app.route('/logout')
#~ def logout():
    #~ # remove the username from the session if it's there
    #~ session.pop('username', None)
    #~ return redirect(url_for('index'))