🧩 Projeto CI/CD com GitHub Actions e Docker

Este projeto tem como objetivo praticar conceitos de DevOps, implementando um pipeline de Integração Contínua (CI) utilizando GitHub Actions, Python (Flask) e Docker.

A aplicação é simples — um Hello World em Flask —, mas o foco principal está na automação de build, testes e deploy via pipeline CI/CD.

🚀 Tecnologias utilizadas

Python 3.10

Flask

Pytest

Docker

GitHub Actions

⚙️ Funcionalidades do pipeline

O pipeline automatiza as seguintes etapas:

Checkout do repositório

Configuração do ambiente Python

Instalação de dependências

Execução de testes automatizados com Pytest

Build da imagem Docker

Login e push da imagem para o Docker Hub

🧪 Testes automatizados

Os testes estão localizados em tests/test_app.py
Eles validam o comportamento básico da aplicação Flask.

Para executar localmente:

pytest

🐳 Docker
Build da imagem
docker build -t nome-usuario/nome-repositorio:latest .

Executar o container
docker run -p 5000:5000 nome-usuario/nome-repositorio:latest


A aplicação ficará disponível em:
👉 http://localhost:5000

⚡ Pipeline CI/CD

O pipeline é executado automaticamente a cada push ou pull request na branch main.

Arquivo de workflow:

.github/workflows/ci.yml

Etapas do workflow:

Instala dependências Python

Executa testes com Pytest

Cria imagem Docker

Faz login e push no Docker Hub

📦 Estrutura do projeto
.
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml

💡 Aprendizados

Durante o desenvolvimento, foram aplicados conceitos fundamentais de CI/CD, automação de testes e integração com Docker Hub, incluindo troubleshooting de falhas reais no pipeline — simulando o fluxo de detecção, correção e reexecução em um ambiente DevOps.
