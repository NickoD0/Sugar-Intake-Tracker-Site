@app.route('/greet/<name>') # specific route with a variable
def hello(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/add/<int:a>/<int:b>') # route with integer variables/dynamic URLs
def add(a, b):
    return f'<h1>{a} + {b} = {a + b}</h1>'

@app.route('/handle_url_params')    # handling url params 
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}, {name}'
    else:
        return "some parameters are missing"
    
@app.route('/admin/') # in case I need an admin page for some reason
def admin():
    return redirect(url_for('home'))