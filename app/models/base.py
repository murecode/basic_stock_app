from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Razon de este fichero:
# por una razón muy clara: centralización y reutilización estructural en proyectos que usan SQLAlchemy. Aquí te explico el porqué:
#¿Qué es declarative_base()?
#Es una fábrica de clases base que permite definir modelos usando la sintaxis declarativa de SQLAlchemy.