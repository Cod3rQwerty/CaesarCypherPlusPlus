#variable and list things
list_of_letters = ['`', 'u', '0', '}', '_', '<', 'E', 'S', 't', "'", '|', 'G', '~', '%', '$', '(', 'B', 'F', 'L', 'T', 'n', 'l', 'b', '^', 'C', '¬', 'z', 'J', 'p', '1', 'N', 'A', '£', '=', 'x', '9', 'd', 'W', '7', '4', 'Q', '"', 'w', '3', '{', 'y', ':', 'g', 'o', '2', '.', '6', '-', 'v', 'K', ',', 'j', 'c', '!', '>', '?', 'R', 'k', ' ', 'q', 'f', 's', ';', 'i', ')', 'O', 'V', 'Y', 'M', '/', 'a', 'X', 'h', ']', 'D', 'e', '*', '&', 'U', '@', 'H', 'I', '[', '+', '8', 'Z', 'P', 'r', '5', 'm', '#']
storage = ""
#functions
def CaesarCipherEncrypt(input_str, key):
    output = ""
    for i in range(len(input_str)):
        output = output + list_of_letters[list_of_letters.index(input_str[i]) - int(key)]
    return output
def CaesarCipherDecrypt(message, key):
    output = ""  # Initialize output inside the function
    input_str = str(message)  # Renamed variable to avoid shadowing built-in function
    for i in range(len(input_str)):
        output = output + str(list_of_letters[list_of_letters.index(input_str[i]) + int(key)])
    return output

#main code
while True:
    try:
        choice = input("Would you like to Encrypt or Decrypt? ").upper()
        if choice != "ENCRYPT" and choice != "DECRYPT":
            print("Please enter either Encrypt or Decrypt.")
        elif choice == "ENCRYPT":
            storage = ""
            text = input("Text: ")
            Key = input("Key: ")
            for i in range(len(text)):
                storage += CaesarCipherEncrypt(text[i], Key[i%len(Key)])
            print("Encrypted Text: " + str(storage))
            storage = ""
        else: # this means its decrypt
            storage = ""
            text = input("Text: ")
            Key = input("Key: ")
            for i in range(len(text)):
                storage += CaesarCipherDecrypt(text[i], Key[i%len(Key)])
            print("Decrypted text: " + str(storage))
            storage = ""
    except:
        print("An Error has occured. Please check your inputs and try again. The key must be an integer.")