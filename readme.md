
# Flask CRUD App
 
## Instalación:
    
    git clone https://github.com/npho111/test_frontend
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Crear database (postgresql en este caso):


    CREATE TABLE Data (
        alumno_ID serial,
        curso_id serial,
        nombre VARCHAR ( 50 ),
        apellido VARCHAR ( 50 ),
        nota INT,	
        primary key (alumno_ID, curso_id)
        );

Crear database en esta locacion o modificar para replicar la app.
[![postgre.png](https://i.postimg.cc/HnxdkVL9/postgre.png)](https://postimg.cc/0MLLt5Dz)

## Utilización:

    python3 app.py


[![image-2022-02-08-074830.png](https://i.postimg.cc/dVf0hMZK/image-2022-02-08-074830.png)](https://postimg.cc/Bjx3zVCh)

[![crudapp2.png](https://i.postimg.cc/YqZ99KWB/crudapp2.png)](https://postimg.cc/kBN91HsT)





