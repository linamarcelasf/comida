from flask import Flask, render_template, request, redirect, url_for, flash
import time

# tiempos

# server
app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "empresa"

def fecha():
    a = time.strftime('%Y-%m-%d %H:%M:%S')
    return a


def mes():
    a = time.strftime('%b')
    return a



# rutas


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/carta")
def carta():
    return render_template('carta.html')

@app.route("/domicilios")
def domicilios():
    return render_template('domicilios.html')
    
@app.route("/ordena_aqui")
def ordena_aqui ():
    return render_template('ordena_aqui.html')

@app.route("/contactanos")
def contactanos():
    return render_template('contactanos.html')


if __name__ == '__main__':
    app.run(debug=True)
