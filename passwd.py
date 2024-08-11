import random
import string

def generate_password(vowels, uppercase, lowercase, digits, special_chars):
    # Définir les ensembles de caractères
    vowel_set = 'aeiou'
    uppercase_set = string.ascii_uppercase
    lowercase_set = string.ascii_lowercase
    digit_set = string.digits
    special_char_set = string.punctuation

    # Créer le mot de passe avec les caractères demandés
    password = (
        random.choices(vowel_set, k=vowels) +
        random.choices(uppercase_set, k=uppercase) +
        random.choices(lowercase_set, k=lowercase) +
        random.choices(digit_set, k=digits) +
        random.choices(special_char_set, k=special_chars)
    )

    # Mélanger les caractères pour éviter toute prévisibilité
    random.shuffle(password)
    
    # Convertir la liste en chaîne de caractères
    return ''.join(password)

def main():
    print("Générateur de mot de passe")
    
    try:
        vowels = int(input("Nombre de voyelles: "))
        uppercase = int(input("Nombre de majuscules: "))
        lowercase = int(input("Nombre de minuscules: "))
        digits = int(input("Nombre de chiffres: "))
        special_chars = int(input("Nombre de caractères spéciaux: "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        return

    # Générer et afficher le mot de passe
    password = generate_password(vowels, uppercase, lowercase, digits, special_chars)
    print(f"Mot de passe généré : {password}")

if __name__ == "__main__":
    main()
