from pydantic import BaseModel
from typing import Optional


class AuditsCreate(BaseModel):
    id_auditoria:  Optional[int] = None
    id_usuario: int
    modulo: Optional[str] = None
    link: Optional[str] = None
    icono: Optional[str] = None
