import httpx
from fastapi import FastAPI, Depends
from ..schemas.SchemaPaciente import RequestPaciente

app = FastAPI()

async def get_cliente():
    async with httpx.AsyncClient() as cliente:
        yield cliente

@app.post("/inserir-paciente", status_code=201)
async def inserir_paciente(paciente: RequestPaciente, cliente: httpx.AsyncClient = Depends(get_cliente)):
    data = {
        'id': paciente.id,
        'nome': paciente.nome,
        'idade': paciente.idade,
        'sexo': paciente.sexo,
        'telefone': paciente.telefone,
        'plano_saude': paciente.plano_saude
    }
    response = await cliente.post("http://localhost:8000/db-inserir-paciente", json=data)
    
    return response.json()

@app.post("/listar-todos-paciente", status_code=201)
async def listar_todos_paciente(cliente: httpx.AsyncClient = Depends(get_cliente)):

    response = await cliente.post("http://localhost:8000/db-listar-todos-paciente")
    
    return response.json()
