# VendasStreamlit
Aplicativo simples utilizando MySql e Streamlit

Funcionalidades
1. Login
Formulário simples com escolha de perfil (vendedor/gerência)
Validação básica

2. Tela do Vendedor
Registrar venda
Nome do cliente (dropdown ou texto)
Produto
Valor
Vendedor (auto preenchido)
Excluir venda
Exibir lista das vendas feitas por ele
Botão de exclusão com confirmação

3. Tela da Gerência
Dashboard com indicadores
Total de vendas
Valor arrecadado
Quantas pessoas pagaram/não pagaram
Buscar cliente
Campo para buscar por nome
Mostrar produtos, valores e status de pagamento
Dar baixa no pagamento
Marcar o cliente como “pago”

4. Banco de Dados
Tabelas básicas:

clientes (id, nome)
vendas (id, cliente_id, produto, valor, vendedor, data, produtopago)
pagamentos (cliente_id, statustotal)

- Estrutura do Projeto

VendasStreamlit/
├── src/
│   ├── auth/              # Autenticação de usuários
│   ├── pages/             # Telas da aplicação
│   ├── database/          # Conexão e consultas MySQL
│   ├── utils/             # Funções auxiliares
│   └── validations/       # Regras de validação
│
├── assets/                # Imagens e ícones
├── config/                # Configurações gerais
├── requirements.txt       # Lista de dependências
├── .env                   # Variáveis de ambiente (não subir para o GitHub)
└── app.py                 # Arquivo principal da aplicação


Para alterações, criar Ambiente virtual com os seguintes comandos no terminal:

cd C:\Users\Aluno\Desktop\VendasStreamlit
python -m venv venv
venv\Scripts\activate

Criamos o ambiente e ativamos, agora vamos baixar as dependências e rodar

pip install -r requirements.txt
streamlit run app.py
