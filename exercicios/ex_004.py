# faça um programa que peça pra escrever algo e mostre o tipo e as expecificassões

word = input('write anything here ------>  ')
print('this word is ', type(word))
print('is upper? = ', (word.isupper()))
print('é minuscula? = ', (word.islower()))
print('é numerico? = ', (word.isnumeric()))
print('é palavra? = ', (word.isalpha()))
print('é alfanumerico? = ', (word.isalnum()))
print('é decimal? = ', (word.isdecimal()))
print('é espaço? = ', (word.isspace()))
