
import json
from api_modelo.schemas.SchemaPaciente import RequestPaciente

class PacienteModel:

    def inserir(self, paciente: RequestPaciente):
            caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta API\api_modelo\models\jsons\PacienteJson.json'

            with open(caminho_arquivo, "r") as saida_json:
                try:
                    json_arquivo = json.load(saida_json)
                except:
                    json_arquivo = None

            if json_arquivo is None:
                json_lista = []
                with open(caminho_arquivo, "r+") as saida_json:
                    json_lista.append(paciente.__dict__)
                    json_arquivo = json.dumps(json_lista)
                    saida_json.write(json_arquivo)
            else:
                with open(caminho_arquivo, "w") as saida_json:
                    pass
                with open(caminho_arquivo, "w") as saida_json:
                    json_arquivo.append(paciente.__dict__)
                    saida_json.write(json.dumps(json_arquivo))
        
    def listar_todos(self):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta API\api_modelo\models\jsons\PacienteJson.json'
        objetos_paciente = []

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                for json_dado in json_arquivo:
                    pacientemodel = PacienteModel()
                    pacientemodel.id = json_dado['id']
                    pacientemodel.nome = json_dado['nome']
                    pacientemodel.idade = json_dado['idade']
                    pacientemodel.sexo = json_dado['sexo']
                    pacientemodel.telefone = json_dado['telefone']
                    pacientemodel.plano_saude = json_dado['plano_saude']
                    objetos_paciente.append(pacientemodel)
                return objetos_paciente
            except:
                pass