from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # importar el operador and y or

# Importamos la clase Pais del archivo genera_base
from genera_base import Pais

# Enlace al gestor de base de datos
engine = create_engine('sqlite:///basepersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los lenguajes de cada país
print("Presentación de los lenguajes de cada país")
lenguajes_pais = session.query(Pais.nombre_pais, Pais.lenguajes).all()
# Colocar en el query los atributos que queremos mostrar
print(lenguajes_pais)