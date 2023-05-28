#4. Implement the code of encryption of affine cipher.
#Name : Dhruba Saha
#Roll : B.Sc(Sem-V)Comp-04


import math

def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    key1 = int(data[0].split("=")[1])
    while math.gcd(key1, 26) != 1:
        print("Error: Key 1 must be coprime with 26.")
        key1 = int(input("Enter a new value for key 1: "))
    key2 = int(data[1].split("=")[1])
    plaintext = data[2].split("=")[1]
    ciphertext = encrypt(plaintext, key1, key2)
    with open("output.txt", "w") as file:
        file.write(ciphertext)
    print("Encrypted text has been written to output.txt.")

def encrypt(plaintext, key1, key2):
    ciphertext = ""
    for i in plaintext:
        if i.isupper():
            ciphertext += chr((key1 * (ord(i) - 65) + key2) % 26 + 65)
        elif i.islower():
            ciphertext += chr((key1 * (ord(i) - 97) + key2) % 26 + 97)
        else:
            ciphertext += i
    return ciphertext

main()