from flask import Flask, render_template, send_from_directory
import random
import os

app=Flask(__name__, template_folder='.', static_folder='.')

def saludo_aleatorio():
    saludos = ['Hola', 'Good morning','Buenas tardes','Buenos dias','Buonasera','Ciao','Privyét','Konnichiwa',
               'Buenas noches','Bonjour','Hallo','Oi','Hi','Hello','Annyeonghaseyo','Merhaba','Selam','Aloha',
               'Shin chao','Bom dia','Nín hǎo','Namaste','Guten Tag','Salut','Привет','안녕하세요','您好','Marhaban']
    return random.choice(saludos)

#@app.route('/')
#def home():
 #   return f"<h1>{saludo_aleatorio()}</h1>"

@app.route('/')
def home():
    saludo = saludo_aleatorio()
    return render_template('index.html', saludo=saludo)

@app.route('/magico.mp3')
def get_audio():
    return send_from_directory(os.getcwd(), 'magico.mp3')


if __name__ == '__main__':
    app.run(debug=True)