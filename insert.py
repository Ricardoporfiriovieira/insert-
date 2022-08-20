i = 0
vetor = [30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
contador = 0
temp = 0
for i in range(1, len(vetor)):
    temp = vetor[i]
    j = i -1
    while(j >= 0 and temp < vetor[j]):
        vetor[j+1] = vetor[j]
        j-=1
    vetor[j+1] = temp

print("vetor ordenado: ", vetor)