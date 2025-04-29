# 🩺 Aplicação de Agendamento de Consultas Com APIs REST

Este repositório contém a implementação de uma aplicação para **agendamento de consultas** com APIs REST, focada na parte de **cadastro de pacientes**.

✅ A estrutura da implementação consiste em **duas APIs REST**: uma responsável pela parte de **modelo** e outra responsável pela **persistência e consulta dos dados**.

👩🏻 O **usuário** realiza solicitações de **inserção** ou **listagem** para a API de modelo, que por sua vez encaminha a requisição para o **endpoint** correspondente da API de persistência e consulta dos dados.

📋 A implementação foi realizada utilizando a linguagem **Python** e a **persistência e cosulta dos dados** foi efetuada em arquivos **JSON**.

## ⚙️ Funcionalidades
- 📋 Inserção e listagem de registros de pacientes
- 🔁 Comunicação entre APIs REST para separação de responsabilidades
- 💾 Persistência dos dados em arquivos **JSON**

## 🛠️ Tecnologias Utilizadas
- Python 🐍
- FastAPI para criação das APIs 🚀
- Arquivos JSON para a persistência dos dados 📄
