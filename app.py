from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



#app = Flask(__nombre__)
#app.secret_key = "Secret Key"
app = Flask(__name__)
app.config['TESTING'] = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/escuela'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for our CRUD database
class Data(db.Model):
    alumno_id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    nota = db.Column(db.Integer)
    def __init__(self, nombre, apellido, nota):
        #self.curso_id = curso_id
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

#donde hacemos query a la data
@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template("index.html", alumnos = all_data)

@app.route('/calendario.html')
def calendario():
    return render_template('calendario.html')

#para insertar data a database con html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        nota = request.form.get('nota')

        my_data = Data(nombre, apellido, nota)
        db.session.add(my_data)
        db.session.commit()

        flash("Alumno Agregado Exitosamente!")

        return redirect(url_for('index'))


#actualizar la tabla
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        
        my_data.nombre = request.form.get('nombre')
        my_data.apellido = request.form.get('apellido')
        my_data.nota = request.form.get('nota')

        db.session.commit()
        flash("Alumno Agregado!")

        return redirect(url_for('index'))

#para eliminar alumno
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Alumno Eliminado!")

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = 'secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)