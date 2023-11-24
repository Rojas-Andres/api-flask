from pydantic import BaseModel
from typing import Optional


class FuncionalidadCreate(BaseModel):
    id_funcionalidad:  Optional[int] = None 
    nombre_funcionalidad: Optional[str] = None
    link: Optional[str] = None
    icono: Optional[str] = None
