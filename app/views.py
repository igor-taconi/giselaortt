from flask import Flask, render_template, request, flash


def init_app(app: Flask) -> Flask:
    @app.route('/')
    def index():
        name = 'Olárrrrrrrrrrrrrrr'
        return render_template('index.html', name=name)

    @app.route('/store')
    def store():
        return render_template('store.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        contact = ''

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            contact = f'<Name {name}> {email}'
            flash('Logado com sucesso!', 'success')

        return render_template('login.html', contact=contact)

    @app.route('/blog')
    def blog():
        return render_template('blog.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    return app
