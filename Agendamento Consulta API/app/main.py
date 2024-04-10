import httpx
import uuid

nome = str(input("Nome: "))
idade = int(input("Idade: "))
sexo = str(input("Sexo: "))
telefone = str(input("Telefone: "))
plano_saude = bool(input("Plano de Saúde: "))

paciente = {
    'id': str(uuid.uuid4()),
    'nome': nome,
    'idade': idade,
    'sexo': sexo,
    'telefone': telefone,
    'plano_saude': plano_saude
}

response_inserir = httpx.post("http://127.0.0.1:8001/inserir-paciente", json=paciente)
print(response_inserir.json())
response_listar = httpx.post("http://127.0.0.1:8001/listar-todos-paciente")
print(response_listar.json())