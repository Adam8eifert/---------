# Projekt 1: Engeto Online Python Academy
# Autor: Adam Seifert

TEXTS = [
    """Situated about 10 miles west of Kemmerer, ...""",
    """At the base of Fossil Butte are the bright ...""",
    """The monument contains 8198 acres and protects ..."""
]

# Uživatelé a jejich hesla
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password",
    "liz": "pass123"
}

# Počet pokusů o přihlášení


# Smyčka pro přihlášení uživatele
for _ in range(3):
    username = input("Enter your username:").strip()
    password = input("Enter your password:").strip()

    # Kontrola, zda bylo vyplněno jméno a heslo
    if not username or not password:
        print("❗ Both username and password are required!")
        continue

    # Kontrola, zda uživatelské jméno začíná malým písmenem
    if not username[0].islower():
        print("❗ Username must start with a lowercase letter!")
        continue

    # Kontrola, zda uživatel existuje
    if username not in users:
        print("❗ Username does not exist!")
        continue

    # Kontrola správnosti hesla
    if users[username] != password:
        print("❗ Incorrect password!")
        continue

    # Úspěšné přihlášení
    print(f"✅ Hello {username}, welcome to the app! We have {len(TEXTS)} texts to be analyzed.")
    break  # Ukončení smyčky při úspěšném přihlášení
else:
    print("❌ Access denied! Too many failed attempts.")



  