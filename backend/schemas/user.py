"""
backend/schemas/user.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Schemas de Usuário

Versão: 1.0

Responsabilidades:

- Validar dados recebidos pela API.
- Preparar cadastro e login.
- Definir formatos de entrada e saída.
"""

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    Dados necessários para cadastro.
    """

    username: str

    email: EmailStr

    password: str



class UserLogin(BaseModel):
    """
    Dados necessários para login.
    """

    email: EmailStr

    password: str



class UserResponse(BaseModel):
    """
    Dados retornados pela API.
    """

    username: str

    email: EmailStr

    active: bool


    class Config:

        from_attributes = True