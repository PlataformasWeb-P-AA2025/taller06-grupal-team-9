from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # importar el operador and y or

# Importamos la clase Pais del archivo genera_base
from genera_base import Pais

# Enlace al gestor de base de datos
engine = create_engine('sqlite:///basepersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países de Asía, ordenados por el atributo Dial
# Aplicamos el filter para obtener los países que pertenecen al continente Asia (AS)
# Y el order_by para ordenarlos por Dial
print("Presentación de los países asiaticos, ordenados por el atributo Dial")
asia_dial = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
# Dial es una cadena, no se ordena por el valor numérico
print(asia_dial)