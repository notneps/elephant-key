import string, secrets
from words import get_word_list

def generate_strong_password(length=16):
    """Generate a strong password of the specified length"""
    characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_easy_password(length=4):
    """Generate an easy password"""
    word_list = get_word_list()    
    password = ''.join(f"{secrets.choice(word_list)} " for _ in range(length))
    password = password.strip()
    return password

def main():
    # for testing purposes only
    good_password = generate_strong_password()
    print("Good password (16 digits):")
    print()
    print(good_password)

    easy_password = generate_easy_password()
    print("Easy to remember password:")
    print()
    print(easy_password)

if __name__ == "__main__":
    main()