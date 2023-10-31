from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/main",
    tags=["main"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello World"})
