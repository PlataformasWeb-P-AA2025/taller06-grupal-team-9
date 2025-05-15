from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

# Importamos la clase Pais del archivo genera_base
from genera_base import Pais

# Enlace al gestor de base de datos
engine = create_engine('sqlite:///basepersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
print('Países cuyo nombre contiene "uador" o su capital contiene "ito":')
paises_filtrados = session.query(Pais).filter(or_(Pais.nombre_pais.like('%uador%'),Pais.capital.like('%ito%'))).all()

for pais in paises_filtrados:
    print(pais)