from domain.commons.rimac_client import RimacClient
from repository.superscore_vida_seguros_rgfvv import get_superscore_vida_seguros_rgfvv


def get_superscore_vida_seguros_rgfvv_use_case(payload: RimacClient) -> dict:
    score = get_superscore_vida_seguros_rgfvv(payload)
    return score.format_response()