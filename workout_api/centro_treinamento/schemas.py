from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Centro de Treinamento", example="CT King", max_length=20),
    ]
    endereco: Annotated[
        str,
        Field(description="Endereço", example="Rua 1, 123", max_length=60),
    ]
    proprietario: Annotated[
        str,
        Field(description="Proprietário", example="João da Silva", max_length=30),
    ]
