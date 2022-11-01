def primeira_posicao_sub_string(string,substring):
    if substring in string:
        return substring[0]
    return -1

string = input('digite a string: ')
substring = input('digite a substring: ')
print(primeira_posicao_sub_string(string,substring))