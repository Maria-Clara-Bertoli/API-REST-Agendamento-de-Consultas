import json
from fastapi import FastAPI
from api_modelo.schemas.SchemaPaciente import RequestPaciente
from api_modelo.models.ModeloPaciente import PacienteModel

pacientemodel = PacienteModel()

app = FastAPI()

@app.post("/db-inserir-paciente", status_code=201)
async def inserir_paciente(paciente: RequestPaciente):
    pacientemodel.inserir(paciente)
    return {"mensagem": "Dados inseridos com sucesso!"}

@app.post("/db-listar-todos-paciente", status_code=201)
async def listar_paciente():
    pacientes = pacientemodel.listar_todos()
    response = json.dumps([paciente.__dict__ for paciente in pacientes])
    return response