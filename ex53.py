def matriz_identidade(vetor,ordem):
    ehIdentidade = False
    if ordem == 1:
        for l in range(0,1):
            if vetor[l] == 1:
               ehIdentidade = True 
    if ordem == 2:
        for l in range(0,2):
            for c in range(0,2):
                if vetor[0][0] == 1 and vetor[1][1] == 1:
                    ehIdentidade = True
    if ordem == 3:
        for l in range(0,3):
            for c in range(0,3):
                if (vetor[0][0] == 1) and (vetor[1][1] == 1) and \
                 vetor[2][2] == 1:
                    ehIdentidade = True
    if ordem == 4:
        for l in range(0,4):
            for c in range(0,4):
                if (vetor[0][0] == 1) and (vetor[1][1] == 1) and \
                   (vetor[2][2] == 1) and (vetor[3][3] == 1):
                    ehIdentidade = True
    elif ordem == 5:
        for l in range(0,5):
            for c in range(0,5):
                if (vetor[0][0] == 1) and (vetor[1][1] == 1) and \
                   (vetor[2][2] == 1) and (vetor[3][3] == 1) and \
                   (vetor[4][4] == 1):
                    ehIdentidade = True
