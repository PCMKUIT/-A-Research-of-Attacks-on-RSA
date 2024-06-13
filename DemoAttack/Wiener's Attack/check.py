def compare_keys():
    try:
        with open('privatekey.pri', 'r') as pri_file:
            pri_key_content = pri_file.read().strip()
    except FileNotFoundError:
        print("Privatekey.pri not found. Please generate keys first.")
        return
    except Exception as e:
        print(f"An error occurred while reading privatekey.pri: {e}")
        return
    
    try:
        with open('privatekey.txt', 'r') as txt_file:
            txt_key_content = txt_file.read().strip()
    except FileNotFoundError:
        print("Privatekey.txt not found. Please attack first before check.")
        return
    except Exception as e:
        print(f"An error occurred while reading privatekey.txt: {e}")
        return
    
    if pri_key_content == txt_key_content:
        print("Attack success with Wiener's Attack! The privatekey is correct!")
    else:
        print("Attack failed with Wiener's Attack! The privatekey is incorrect!")

if __name__ == '__main__':
    compare_keys()
