from models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from security import SECRET_KEY, ALGORITHM, oauth2_schema

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)

def pegar_sessao():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario: str = dic_info.get('sub')
        if id_usuario is None:
            raise HTTPException(status_code=401, detail="Token inválido, 'sub' não encontrado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
    usuario = session.query(Usuario).filter(Usuario.id==int(id_usuario)).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario