"""
backend/services/user_service.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Serviço de Usuários

Versão: 2.0

Responsabilidades:

- Cadastro de usuários.
- Login de usuários.
- Consulta de usuários.
- Persistência no PostgreSQL.
"""

from typing import Optional

from sqlalchemy.orm import Session

from backend.models.user import User


class UserService:

    def create_user(
        self,
        db: Session,
        username: str,
        email: str,
        password_hash: str
    ) -> User:

        usuario = (

            db.query(User)

            .filter(User.email == email)

            .first()

        )

        if usuario:

            raise ValueError(

                "Usuário já cadastrado."

            )

        novo_usuario = User(

            username=username,

            email=email,

            password_hash=password_hash,

            active=True

        )

        db.add(

            novo_usuario

        )

        db.commit()

        db.refresh(

            novo_usuario

        )

        return novo_usuario


    def get_user(
        self,
        db: Session,
        email: str
    ) -> Optional[User]:

        return (

            db.query(User)

            .filter(User.email == email)

            .first()

        )


    def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str
    ) -> Optional[User]:

        usuario = self.get_user(

            db,

            email

        )

        if not usuario:

            return None

        if usuario.password_hash != password:

            return None

        return usuario