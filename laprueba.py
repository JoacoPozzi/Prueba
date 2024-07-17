@app.route('/')
def index():
    return render_template('index.html', menu=menu)
