from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"
def ceaser(again):
    result = ""
    while again.lower() == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        result = ""
        if direction == "encode":
            for char in text:
                if char in alphabet:
                    index = (alphabet.index(char) + shift) % len(alphabet)
                    result += alphabet[index]
                else:
                    result += char
            print(f"Here is the encoded result: {result}")
            again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        elif direction == "decode":
            for char in text:
                if char in alphabet:
                    index = (alphabet.index(char) - shift) % len(alphabet)
                    result += alphabet[index]
                else:
                    result += char
            print(f"Here is the decoded result: {result}")
            again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        else:
            again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    else:
            print("Goodbye")
            exit()
ceaser(again)
