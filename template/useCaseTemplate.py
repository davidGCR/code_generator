from domain.commons.rimac_client import RimacClient
from repository.{{filename}} import get_{{filename}}


def get_{{filename}}_use_case(payload: RimacClient) -> dict:
    score = get_{{filename}}(payload)
    return score.format_response()
