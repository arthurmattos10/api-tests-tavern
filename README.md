# 🧪 API Testing Project – Tavern & FastAPI

Projeto de automação de testes de API desenvolvido como desafio prático, cobrindo testes de contrato, testes assíncronos e boas práticas de versionamento.

---

## 🚀 Tecnologias utilizadas

* Python 3.12
* Pytest
* Tavern
* FastAPI
* HTTPX
* Pytest-asyncio

---

## 📌 Funcionalidades implementadas

### ✅ Testes de contrato (Tavern)

* Testes declarativos em YAML
* Parametrização de cenários
* Encadeamento de dados entre requisições
* Validação customizada com Python

### ✅ Testes de performance assíncrona

* API construída com FastAPI
* Execução concorrente com asyncio
* Testes com múltiplas requisições simultâneas (5, 20, 50)
* Validação de tempo de resposta

### ✅ Boas práticas de repositório

* Uso de `.gitignore`
* Exclusão de arquivos de cache
* Estrutura organizada de projeto

---

## 📂 Estrutura do projeto

```
.
├── api_pagamentos.py
├── test_performance.py
├── test_fluxo_todos.tavern.yaml
├── utils.py
├── __init__.py
├── .gitignore
```

---

## ▶️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install pytest tavern[pytest] fastapi httpx pytest-asyncio
```

### 2. Rodar os testes

```bash
python -m pytest -v
```

---

## 🧠 Conceitos aplicados

* Testes de API REST
* Testes assíncronos
* Concorrência com asyncio
* Testes de contrato
* Integração entre YAML e Python
* Boas práticas com Git

---

## 💡 Objetivo

Demonstrar conhecimentos em automação de testes de API, incluindo validação funcional e testes de performance em ambientes assíncronos.

---

## 👨‍💻 Autor

Arthur Matos Rocha
