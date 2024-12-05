# uloz
jmeno = "Lukáš"

# Ulož příjmení Dvořák
prijmeni = "Dvořák"

# Vytvoř proměnnou "cele_jmeno" obsahující mezeru
cele_jmeno = jmeno + " " + prijmeni

# Vytvoř a vypiš hodnotu délky uložené proměnné "cele_jmeno"
delka_jmena = len(cele_jmeno)
print("Délka jmena:", delka_jmena)

# Vypiš celé jméno ohraničené oddělovači
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)