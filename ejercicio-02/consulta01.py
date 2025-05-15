from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # importar el operador and y or

# Importamos la clase Pais del archivo genera_base
from genera_base import Pais

# Enlace al gestor de base de datos
engine = create_engine('sqlite:///basepersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países del continente americano
# Aplicamos el filter para obtener los países que pertenecen al continente Americano
# Como podemos observar de la base de datos hay una división en el continente americano
# - NA -> América del Norte
# - SA -> América del Sur
print("Presentación de los países del continente americano")
paises_america = session.query(Pais).filter(or_(Pais.continente=="NA", Pais.continente=="SA")).all()
# Debido a la división en NA y SA, se hace uso del or
print(paises_america)