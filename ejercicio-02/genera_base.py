from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepersonas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return ("País: %s Capital: %s Continente: %s Dial: %s Geoname ID: %d ITU: %s Lenguajes: %s Es indepentdiente: %s" 
                % (self.nombre_pais,
                   self.capital,
                   self.continente,
                   self.dial,
                   self.geoname_id,
                   self.itu,
                   self.lenguajes,
                   self.independiente))

Base.metadata.create_all(engine)

