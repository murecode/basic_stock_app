from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

# --- Configuración de la Base de Datos ---
# URL de la base de datos SQLite. se creará un archivo en el mismo directorio.
SQLALCHEMY_DATABASE_URL = "sqlite:///./basic_stock_app.db"

# Crear el motor de la base de datos de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear una clase SessionLocal para cada sesión de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

