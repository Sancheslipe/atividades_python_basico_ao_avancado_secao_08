def intercalar_strings(str1,str2):
    tamanho = int(len(str1+str2 ) // 2)
    palavra = str1
    str1 = ''
    for l in range(0, tamanho):
        str1 += palavra[l] + str2[l]
        
    return str1
    
palavra1 = input(' digite uma palavra: ')
palavra2 = input('digite uma palavra: ')

print(intercalar_strings(palavra1,palavra2))