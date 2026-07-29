"""
backend/routers/users.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Rotas de Usuários

Versão: 2.0

Responsabilidades:

- Cadastro de usuários.
- Login de usuários.
- Consulta de usuário.
- Autenticação com PostgreSQL.
"""

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from backend.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)

from backend.services.user_service import (
    UserService
)

from backend.database.connection import get_db


router = APIRouter(

    prefix="/users",

    tags=["Users"]

)


user_service = UserService()



@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(

    user: UserCreate,

    db: Session = Depends(get_db)

):

    try:

        novo_usuario = user_service.create_user(

            db=db,

            username=user.username,

            email=user.email,

            password_hash=user.password

        )


        return novo_usuario


    except ValueError as erro:

        raise HTTPException(

            status_code=400,

            detail=str(erro)

        )



@router.post(
    "/login"
)
def login_user(

    user: UserLogin,

    db: Session = Depends(get_db)

):

    usuario = user_service.authenticate_user(

        db=db,

        email=user.email,

        password=user.password

    )


    if not usuario:

        raise HTTPException(

            status_code=401,

            detail="Email ou senha inválidos"

        )


    return {

        "status": "success",

        "message": "Login realizado com sucesso",

        "user": {

            "username": usuario.username,

            "email": usuario.email

        }

    }



@router.get(
    "/{email}",
    response_model=UserResponse
)
def get_user(

    email: str,

    db: Session = Depends(get_db)

):

    usuario = user_service.get_user(

        db,

        email

    )


    if not usuario:

        raise HTTPException(

            status_code=404,

            detail="Usuário não encontrado"

        )


    return usuario