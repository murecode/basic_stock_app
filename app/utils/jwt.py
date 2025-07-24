import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta

SECRET_KEY = "my_secret_key" # Esta se debe poner en environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tiempo de expiración del token en minutos


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:

  if expires_delta:
    expire = datetime.utcnow() + expires_delta # Si se proporciona un delta de expiración, se usa
  else:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Expira en 15 minutos por defecto

  # Copiar los datos originales para no modificar el original
  data_to_encode = data.copy()
  # Agregar la fecha de expiración al token
  data_to_encode.update({"exp": expire})

  #Codificar el token con la clave secreta y el algoritmo
  token = jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return token


def decode_jwt_token(token: str) -> dict:
  try:
    # Decodificar el token usando la clave secreta y el algoritmo
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except ExpiredSignatureError:
    raise InvalidTokenError("Token expirado")
  except InvalidTokenError:
    raise InvalidTokenError("Token inválido")