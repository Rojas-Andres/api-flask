from pydantic import BaseModel
from typing import Optional


class FuncionalidadCreate(BaseModel):
    id_funcionalidad: int
    nombre_funcionalidad: Optional[str] = None
    link: Optional[str] = None
    icono: Optional[str] = None


class FuncionalidadUpdate(BaseModel):
    nombre_funcionalidad: Optional[str] = None
    link: Optional[str] = None
    icono: Optional[str] = None
