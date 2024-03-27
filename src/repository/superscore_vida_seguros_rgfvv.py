from domain.commons.rimac_client import RimacClient
from repository.rimac_client_repository import get_prediction
from domain.superscore_vida_seguros_rgfvv.superscore_vida_seguros_rgfvv_response import SuperscoreVidaSegurosRgfvv

QUERY_NAME = "bl_superscore_vida_seguros_rgffvv"

def get_superscore_vida_seguros_rgfvv(payload: RimacClient) -> SuperscoreVidaSegurosRgfvv:
    response = get_prediction(payload, QUERY_NAME)
    return SuperscoreVidaSegurosRgfvv(**response)