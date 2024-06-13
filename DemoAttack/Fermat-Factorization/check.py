def check_fermat_attack_result():
    try:
        with open('factor.txt', 'r') as file_factor:
            factor_content = file_factor.read().strip()
    except FileNotFoundError:
        print("Factor.txt not found. Please generate first.")
        return

    try:
        with open('fermat.txt', 'r') as file_fermat:
            fermat_content = file_fermat.read().strip()
    except FileNotFoundError:
        print("Fermat.txt not found. Please attack first before check.")
        return

    if factor_content == fermat_content:
        print("Attack success with Fermat's Attack! Factors are correct!")
    else:
        print("Attack failed with Fermat's Attack! Factors are incorrect!")

def main():
    check_fermat_attack_result()

if __name__ == '__main__':
    main()
