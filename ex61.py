def anagrama(string, anagrama):
    stringTest = string
    teste = True
    
    for t in range(0,len(string)):
        if stringTest[t] not in anagrama:
            teste = False
       
    
    return teste

stringParaTeste = input('digite uma palavra que você gostaria de testar: ')
PalavraAnagrama = input('digite o "anagrama": ')
print(anagrama(stringParaTeste, PalavraAnagrama))