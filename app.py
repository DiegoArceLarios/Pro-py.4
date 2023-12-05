# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():
    titulo = 'Mis datos'
    relacion = 'Soy yo'
    name = "Diego" # escribe tu nombre
    age = "15" # escribe tu edad
    image = '../static/me.jpg'
    return render_template('index.html' , name = name , age = age, image = image, titulo = titulo, relacion = relacion)

# define la ruta a la página web de tu padre.
@app.route('/papa')
def papa():
    titulo = 'Datos de mi papá'
    relacion = 'Relación : Padre'
    name = 'Ivan'
    age = '52'
    image = '../static/father.jpg'
    return render_template('index.html', name = name, age = age, image = image, titulo = titulo, relacion = relacion)

# define la ruta a la página web de tu madre.
@app.route('/mama')
def mama():
    titulo = 'Datos de mi mamá'
    relacion = 'Relación: Madre'
    name = 'Erika'
    age = '45'
    image = '../static/mother.jpeg'
    return render_template('index.html', image = image, relacion = relacion, titulo = titulo, name = name, age = age)

# define la ruta a la página web de tus amigos.
@app.route('/amigo')
def amigo():
    titulo = 'Datos de mi amigo'
    relacion = 'Relación: Amistad'
    age = '15'
    image = '../static/friend.jpg'
    name = 'Jafet'
    return render_template('index.html', image = image, relacion = relacion, name = name, age = age, titulo = titulo)

# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
