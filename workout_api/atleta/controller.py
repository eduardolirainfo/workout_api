from fastapi import APIRouter, status
from workout_api.atleta.schemas import AtletaIn
from workout_api.contrib.dependencies import DatabaseDependency


router = APIRouter()


@router.post(
    "/",
    response_description="Atleta criado com sucesso",
    summary="Cria um novo atleta",
    status_code=status.HTTP_201_CREATED,
)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn):
    pass
