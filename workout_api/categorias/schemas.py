from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[
        str, Field(description="Categoria", example="Puxador", max_length=10)
    ]
