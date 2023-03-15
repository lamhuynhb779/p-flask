from flask import Flask

from markupsafe import escape

from flask import url_for

from flask import request

from flask import render_template

from markupsafe import Markup

from werkzeug.utils import secure_filename

from flask import make_response

from flask import abort, redirect

from flask import session

import secrets

from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Index Page"

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# @app.route("/user/<username>")
# def show_user_profile(username):
#     # Show the user profile for that user
#     return f"User {escape(username)}"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f"Post {escape(post_id)}"

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# -----------------------------------------------------------

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index')) # hàm tạo ta url: url_for
#     print(url_for('login'))
#     print(url_for('login', next = '/'))
#     print(url_for('profile', username='Lam Huynh'))
    
# -----------------------------------------------------------
# Cách 1: Gom lại 1 hàm duy nhất
# def do_the_login():
#     return "Login success"

# def show_the_login_form():
#     return "show login form"

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# Cách 2: Tách ra 2 method riêng biệt cho GET vs POST
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# -----------------------------------------------------------
# File tĩnh thường sẽ đặt trong folder /static
# Tạo url cho file tĩnh (js, css,...)
# with app.test_request_context():
#     print(url_for('static', filename = 'common.css'))

# -----------------------------------------------------------
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name = None):
#     # Thư viện dùng để đánh dấu các biến là an toàn
#     item = Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
#     item1 = Markup('<blink>hacker</blink>')
#     item2 = Markup.escape('<blink>hacker</blink>')
#     item3 = Markup('<em>Marked up</em> &raquo; HTML').striptags()

#     return render_template(
#         'hello.html', 
#         name = name, 
#         item = item, 
#         item1 = item1, 
#         item2 = item2, 
#         item3 = item3
#     )

# -----------------------------------------------------------
# Context Locals
# with app.test_request_context('/hello', method = 'POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method =='POST'

# with app.request_context(environ):
#     assert request.method == 'POST'

# -----------------------------------------------------------
# The Request Object
# def valid_login(username, password):
#     if username == 'lam' and password == '12345':
#         return True
#     return False

# def login_the_user_in(username):
#     # return render_template('dashboard.html', username = username)
#     # Redirects and Errors
#     return redirect(url_for('dashboard', username = username))

# @app.get('/login')
# @app.post('/login')
# def login():
#     error = None
#     # URL?key=value
#     # searchword = request.args.get('key', '')

#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return login_the_user_in(request.form['username'])
#         else:
#             abort(401) # below code will not be executed
#             error = 'Invalid username/password'
#     return render_template('login.html', error = error)

# @app.post('/upload')
# def upload_file():
#     success = False
#     username = request.args.get('username', '')
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"./uploads/{secure_filename(file.filename)}")
#         success = True
#     return render_template('dashboard.html', username = username, success = success)

# @app.get('/get-cookie')
# def read_cookie():
#     # use cookies.get(key) instead of cookies[key] to not get a
#     # KeyError if the cookie is missing.
#     key = request.cookies.get('key')
#     return key

# @app.get('/set-cookie')
# def set_cookie():
#     resp = make_response(render_template('cookie.html'))
#     resp.set_cookie('key', 'secret')
#     return resp

# @app.get('/dashboard')
# def dashboard():
#     username = request.args.get('username', '')
#     return render_template('dashboard.html', username = username)

# # @app.errorhandler(404)
# # def page_not_found(error):
# #     return render_template('page_not_found.html'), 404

# # -----------------------------------------------------------
# # About Responses
# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('page_not_found.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp

# -----------------------------------------------------------
# APIs with JSON
# @app.route('/me')
# def me_api():
#     user = get_current_user()
#     return {
#         'username': user.username,
#         'theme': user.theme,
#         'image': url_for('user_image', filename = user.image)
#     }

# @app.route('/users')
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users ]

# -----------------------------------------------------------
# Session
# Set secret key to some random bytes. Keep this really secret!

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    app.logger.info("User access index page")
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.info("User access login page")
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# -----------------------------------------------------------
# How to generate good secret keys
print(secrets.token_hex())

# -----------------------------------------------------------
# Hooking in WSGI Middleware
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
