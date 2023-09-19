from flask import Flask, render_template, g,  request, session, abort, flash, redirect, url_for

app = Flask("Meu app")
app.config['SECRET_KEY'] = 'pudim'

posts = [
    {
    "titulo": "Minha primeira postagem",
    "texto": "teste"
    },
    {
    "titulo": "Meu segundo post",
    "texto": "teste outro"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts #Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == "admin" and request.form['password'] == "admin":
            session['logado'] = True
            flash("Login efetuado com sucesso!")
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"        
    return render_template('login.html', erro=erro)
