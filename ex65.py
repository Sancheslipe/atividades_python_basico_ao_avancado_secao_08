from asyncio.windows_events import NULL
# o exercicio pediu para retornar o str1 como NULL

def exercicio65(str1,str2,N):
    palavraCompleta = str1 +str2[:N]
    print(palavraCompleta)
    str1 = NULL
    return str1
    #não sei porque mais o null é igual a 0 
palavra1 = input('digite a palavra 1 : ')
palavra2 = input('digite a palavra 2: ')
num = input('digite um numero')
if num.isdigit():
    num = int(num)
else:
    print('digite um numero válido')

print(exercicio65(palavra1,palavra2, num))