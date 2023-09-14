from flask import Flask, render_template

app = Flask("Meu app")


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
