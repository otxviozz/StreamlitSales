users = {
    "gerencia": {"password": "1234", "type": "management"},
    "vendedor": {"password": "abcd", "type": "seller"}
}

def login_verification(username, password):
    if username in users:
        if users[username]["password"] == password:
            return users[username]["type"]
        else:
            return "Senha incorreta!"
    else:
        return "Usuário não encontrado!"