def shifter(letter,alphabet,shift):
    if alphabet.index(letter) + shift > len(alphabet):
        return alphabet[alphabet.index(letter) + shift - len(alphabet)]
    else:
        return alphabet[alphabet.index(letter) + shift]

shift = 0

english_alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
english_alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cipher_text = open('cipher_text.txt', 'w')


for line in open('text.txt','r'):
    shift += 1
    for letter in line:
        if letter.islower():
            cipher_text.write(shifter(letter,english_alphabet_lower,shift))
        elif letter.isupper():
            cipher_text.write(shifter(letter,english_alphabet_upper,shift))
    cipher_text.write('\n')
    
cipher_text.close()