from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # importar el operador and y or

# Importamos la clase Pais del archivo genera_base
from genera_base import Pais

# Enlace al gestor de base de datos
engine = create_engine('sqlite:///basepersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
print("Presentación de los países europeos ordenados por la capital")
capital_europa = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()
# Primero hacemos un filter para los países de Europa, para después ordenarlos por la capital.
print(capital_europa)