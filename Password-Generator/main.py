from src.generator import generate_password
from src.utils import get_yes_no_input
from src.validator import validate_length


def main():
    print("=" *40)
    print('Password Generator')
    print("=" *40)

    try :
        length = int(input("Enter password length"))
        validate_length(length)
        use_numbers = get_yes_no_input('Include symbols? (Y/N):')
        use_symbols = get_yes_no_input("Include symbols? (Y/N):")

        password = generate_password(
            length,
            use_numbers,
            use_symbols
        )
        print("\n Generated Password : ")
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()





