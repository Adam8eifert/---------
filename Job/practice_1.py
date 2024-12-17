# Předdefinovaná data uživatelů
users = {
    "admin": "password123",
    "user1": "mypassword",
    "user2": "securepass"
}

def verify_user(username, password):
    """Funkce pro ověření uživatelského jména a hesla."""
    if username in users and users[username] == password:
        return True
    return False

# Získání uživatelských vstupů
input_username = input("Zadejte uživatelské jméno: ")
input_password = input("Zadejte heslo: ")

# Ověření přihlašovacích údajů
if verify_user(input_username, input_password):
    print("Přihlášení úspěšné!")
else:
    print("Nesprávné uživatelské jméno nebo heslo.")
