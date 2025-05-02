# VendasStreamlit
Aplicativo simples utilizando MySql e Streamlit

Esqueleto do Projeto
A aplicação seguirá esta sequência:

app.py

Carrega Streamlit

Gerencia o estado da sessão (usuário logado ou não)

Direciona para a página correta (login, vendedor, gerência)

auth/

Função de verificação de login (usuário/senha simples ou em banco)

Pode ter perfis diferenciados: "gerência" ou "vendedor"

pages/

login.py: Tela de login

vendedor.py: Tela de registrar venda e excluir venda

gerencia.py: Painel de supervisão com métricas e ações de baixa de pagamento

database/

Conexão com MySQL

Funções para insert, select, delete, update nas tabelas necessárias

validations/

Checar campos obrigatórios

Validar formatos de dados (ex: valor numérico, nome não vazio)

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
