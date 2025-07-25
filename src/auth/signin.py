from src.database.connection import get_connection

def login_verification(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return user["tipo"]
    else:
        return "Usuário ou senha incorretos!"