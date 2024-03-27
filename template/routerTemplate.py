from fastapi import APIRouter
from starlette.responses import JSONResponse
import rlog
from domain.commons.rimac_client import RimacClientRequest
from use_cases.{{filename}} import get_{{filename}}_use_case

BASE_PATH = '{{basepath}}'

router = APIRouter(
    prefix=BASE_PATH
)

@router.post('{{path}}')
@rlog.router(timeout=10.0)
def get_{{filename}}(request: RimacClientRequest):
    response = get_{{filename}}_use_case(request.payload)
    return JSONResponse(response, headers={'status_code': '200'})