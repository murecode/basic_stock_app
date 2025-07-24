import bcrypt


def hash_password(password: str) -> str:
  # Generar sal
  salt = bcrypt.gensalt()
  # Se genera el Hash de la contraseña y se une con la sal
  hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed.decode('utf-8')

# Verificar si la contraseña ingresada en texto plano coincide con el hash
def verify_password(password: str, hashed: str) -> bool:
  return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')) 


