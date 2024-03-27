from pydantic import BaseModel


class {{domainFilename}}(BaseModel):
    scr_superscore_vidaseg_ffvv: str
    per_propension_vidaseg_ffvv_cls: float
    dec_propension_vidaseg_ffvv_cls: int
    model_version: str

    def format_response(self):
        return {
            "score_general": self.scr_superscore_vidaseg_ffvv,
            "detalle": {
                "persistencia": {
                    "score": None,
                    "probabilidad": None,
                    "decil": None,
                    "model_version": None
                },
                "propension": {
                    "score": self.scr_superscore_vidaseg_ffvv,
                    "probabilidad": self.per_propension_vidaseg_ffvv_cls,
                    "decil": self.dec_propension_vidaseg_ffvv_cls,
                    "model_version": self.model_version
                }
            }
        }