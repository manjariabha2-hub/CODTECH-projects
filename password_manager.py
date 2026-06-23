import json
import os
import hashlib
import base64
import secrets
import string


VAULT_FILE = "vault.json"


# ---------- Encryption ----------

def generate_key(master_password):

    return hashlib.sha256(
        master_password.encode()
    ).digest()



def encrypt(text, key):

    data = text.encode()

    encrypted = []

    for i in range(len(data)):

        encrypted.append(
            data[i] ^ key[i % len(key)]
        )


    return base64.b64encode(
        bytes(encrypted)
    ).decode()



def decrypt(text, key):

    data = base64.b64decode(text)

    decrypted = []

    for i in range(len(data)):

        decrypted.append(
            data[i] ^ key[i % len(key)]
        )


    return bytes(decrypted).decode()



# ---------- Storage ----------

def load_vault(key):

    if not os.path.exists(VAULT_FILE):

        return {}


    with open(VAULT_FILE,"r") as file:

        encrypted = json.load(file)



    vault = {}


    for website,data in encrypted.items():

        vault[website] = {

            "username":
            decrypt(
                data["username"],
                key
            ),

            "password":
            decrypt(
                data["password"],
                key
            )

        }


    return vault



def save_vault(vault,key):

    encrypted = {}


    for website,data in vault.items():

        encrypted[website] = {

            "username":
            encrypt(
                data["username"],
                key
            ),

            "password":
            encrypt(
                data["password"],
                key
            )

        }


    with open(VAULT_FILE,"w") as file:

        json.dump(
            encrypted,
            file,
            indent=4
        )



# ---------- Password Generator ----------

def generate_password():

    characters = (
        string.ascii_letters
        +
        string.digits
        +
        "!@#$%^&*"
    )


    return "".join(
        secrets.choice(characters)
        for i in range(16)
    )



# ---------- Menu ----------

def main():

    print("""
============================
      PASSWORD MANAGER
============================
""")


    master = input(
        "Enter master password: "
    )


    key = generate_key(master)


    vault = load_vault(key)



    while True:


        print("""
1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Generate Password
6. Exit
""")


        choice = input(
            "Select option: "
        )



        if choice == "1":

            website = input(
                "Website: "
            )

            username = input(
                "Username: "
            )

            password = input(
                "Password(blank = generate): "
            )


            if password == "":

                password = generate_password()

                print(
                    "Generated:",
                    password
                )


            vault[website] = {

                "username": username,

                "password": password

            }


            save_vault(
                vault,
                key
            )


            print(
                "Saved successfully!"
            )



        elif choice == "2":


            if not vault:

                print(
                    "No passwords saved"
                )

            else:

                for website,data in vault.items():

                    print("----------------")

                    print(
                        "Website:",
                        website
                    )

                    print(
                        "Username:",
                        data["username"]
                    )

                    print(
                        "Password:",
                        data["password"]
                    )



        elif choice == "3":

            search = input(
                "Search website: "
            )


            for website,data in vault.items():

                if search.lower() in website.lower():

                    print("----------------")

                    print(
                        "Website:",
                        website
                    )

                    print(
                        "Username:",
                        data["username"]
                    )

                    print(
                        "Password:",
                        data["password"]
                    )



        elif choice == "4":

            website = input(
                "Delete website: "
            )


            if website in vault:

                del vault[website]

                save_vault(
                    vault,
                    key
                )

                print(
                    "Deleted"
                )

            else:

                print(
                    "Not found"
                )



        elif choice == "5":

            print(
                "Generated Password:",
                generate_password()
            )



        elif choice == "6":

            print(
                "Goodbye!"
            )

            break



        else:

            print(
                "Invalid choice"
            )



if __name__ == "__main__":

    main()