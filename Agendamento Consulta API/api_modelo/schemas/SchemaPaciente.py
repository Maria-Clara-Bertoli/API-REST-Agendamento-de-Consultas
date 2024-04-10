from pydantic import BaseModel

class RequestPaciente(BaseModel):
    id: str
    nome: str
    idade: int 
    sexo: str
    telefone: str
    plano_saude: bool