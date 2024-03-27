from fastapi import APIRouter
from starlette.responses import JSONResponse
import rlog
from domain.commons.rimac_client import RimacClientRequest
from use_cases.superscore_vida_seguros_rgfvv import get_superscore_vida_seguros_rgfvv_use_case

BASE_PATH = 'super-score'

router = APIRouter(
    prefix=BASE_PATH
)

@router.post('renta-garantizada/general')
@rlog.router(timeout=10.0)
def get_superscore_vida_seguros_rgfvv(request: RimacClientRequest):
    response = get_superscore_vida_seguros_rgfvv_use_case(request.payload)
    return JSONResponse(response, headers={'status_code': '200'})