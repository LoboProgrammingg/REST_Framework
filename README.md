# 🌐 REST Framework

Este repositório contém a implementação de uma API RESTful utilizando **Python** e frameworks modernos para desenvolvimento web. Ele é projetado para ser flexível, escalável e fácil de usar em projetos de pequeno a grande porte.

---

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Django REST Framework**: Framework poderoso e flexível para construção de APIs.
- **HTML**: Para visualizações e documentação interativa das APIs.
- **JavaScript**: Para interações dinâmicas e suporte a clientes RESTful.
- **Outras Ferramentas**: Inclui bibliotecas auxiliares para otimizar o desenvolvimento.

---

## 🛠️ Funcionalidades

- 🔹 Criação, leitura, atualização e exclusão (CRUD) de recursos.
- 🔹 Autenticação e autorização utilizando **JWT**.
- 🔹 Suporte para **serialização complexa** e validação de dados.
- 🔹 Paginação, filtros e ordenação de resultados.
- 🔹 Testes automatizados para validação de endpoints.
- 🔹 Documentação interativa com **Swagger** e **Redoc**.

---

## 📦 Como Configurar o Projeto?

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### Passos para Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/LoboProgrammingg/REST_Framework.git
   cd REST_Framework
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

---

## 🧪 Testes

Execute os testes automatizados para garantir que tudo está funcionando conforme esperado:

```bash
python manage.py test
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adicionei uma nova feature'
   ```
4. Envie para a branch principal:
   ```bash
   git push origin minha-feature
   ```
5. Crie um Pull Request.
