from domain.commons.rimac_client import RimacClient
from repository.rimac_client_repository import get_prediction
from domain.{{filename}}.{{filename}}_response import {{domainFilename}}

QUERY_NAME = "{{queryName}}"

def get_{{filename}}(payload: RimacClient) -> {{domainFilename}}:
    response = get_prediction(payload, QUERY_NAME)
    return {{domainFilename}}(**response)