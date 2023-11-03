from typing import Annotated
from pydantic import Field, PositiveFloat, PositiveInt
from workout_api.contrib.schemas import BaseSchema


class AtletaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do Atleta", example="João", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do Atleta", example="12345678910", max_length=11)
    ]
    idade: Annotated[PositiveInt, Field(description="Idade do Atleta", example=20)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example=80.5)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do Atleta", example=1.80)
    ]
    sexo: Annotated[
        str, Field(description="Gênero do Atleta", example="M", max_length=1)
    ]
