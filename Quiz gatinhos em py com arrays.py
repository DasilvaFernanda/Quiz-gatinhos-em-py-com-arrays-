# Author: Fernanda

quiz1 = "Quanto tempo vive um gato? \n(A) 12-18 anos \n(B) 15-18 anos \n(C) 10-13 anos"
quiz2 = "Gatos gostam de sorvete? \n(A) sim \n(B) não \n(C) com certeza"
quiz3 = "Qual a cor de gato mais bonita? \n(A) Marrom \n(B) Preto \n(C) Branco"

menu = [quiz1,quiz2,quiz3]
ans = ["A","A","B"] #respostas
score = 0

print ("Bem vindo ao quiz sobre gatinhos!")
answer_user = input("vamos lá? (S/N)")
if answer_user.upper() == "S":
    i=0
    print("Começando...")
    while i < len(menu):
        print(menu[i])
        answer_user = input(" ") #A B C
        if ans[i] == answer_user.upper():
            print("Resposta Correta!")
            score+=10 # soma 10 no score
        else:
            print("Resposta Incorreta!")
        i+=1 # i = i +1
        
print("Score Final: %i"%score) #Game Over
        
