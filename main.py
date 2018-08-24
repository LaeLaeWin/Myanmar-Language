from flask import Flask , render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/ztou.html')
def ztou():
    return render_template('ztou.html')

@app.route('/ztow.html')
def ztow():
    return render_template('ztow.html')

@app.route('/wtou.html')
def wtou():
    return render_template('wtou.html')

@app.route('/wtoz.html')
def wtoz():
    return render_template('wtoz.html')

@app.route('/utow.html')
def utow():
    return render_template('utow.html')

@app.route('/utoz.html')
def utoz():
    return render_template('utoz.html')

@app.route('/signup1.html')
def signup1():
    return render_template('signup1.html')

@app.route('/signin1.html')
def signin1():
    return render_template('signin1.html')

if __name__ == '__main__':
    app.run(debug=True)
