# IBAN number validator
aakkoset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Function clean the input and convert it to a number
def KasitteleNumero(number):
    number = number.replace(" ", "")
    if len(number) == 18:
        Nelja = number[:4]
        Loput = number[4:]
        Lopullinen = Loput + Nelja
        for x in Lopullinen:
            if x in aakkoset:
                n = get_alphabet_order(x) + 9
                Lopullinen = Lopullinen.replace(x, str(n))
        Lopullinen = int(Lopullinen)
        return Lopullinen
    else:
        return "Invalid IBAN number"

# Function to get the order of the alphabet to convert to numbers
def get_alphabet_order(alphabet):
    if len(alphabet) != 1:
        return None  # Return None if input is not a single alphabet character

    if 'A' <= alphabet <= 'Z':
        base_code_point = ord('A')  # Base code point for uppercase letters
    elif 'a' <= alphabet <= 'z':
        base_code_point = ord('a')  # Base code point for lowercase letters
    else:
        return None  # Return None if input is not an alphabet character

    return ord(alphabet) - base_code_point + 1

# Function to check if the IBAN number is valid
def isvalid(Numero):
    if Numero % 97 == 1:
        return True
    else:
        return False


#Mainloop to ask the user for IBAN number
while True:
    print("Enter the IBAN number: ")
    T = input()

    Numero = KasitteleNumero(T)
    #Check if the input is valid
    if Numero != "Invalid IBAN number":
        OnkoIBAN = isvalid(Numero)
        if OnkoIBAN == True:
            print(OnkoIBAN, " IBAN is valid")
        else:
            print(OnkoIBAN, " IBAN is invalid")
    else:
        print(Numero)