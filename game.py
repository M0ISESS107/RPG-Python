from personagem import *
from boss import *
import random


class ficha():
    nome=input("Digite o nome do seu personagem:\n")
    idade=int(input("Digite a idade do seu personagem: \n"))
    escolha=int(input("Digite 1- Para Mago ou 2- Para Guerreiro \n"))
    persona=personagem(nome,idade,escolha)
    classe,vida,ataque,defesa=persona.classes()
    print("esse e seu personagem:\n")
    print(f"NOME: {nome}\nIDADE: {idade}\nCLASSE: {classe}\nVIDA: {vida}\nATAQUE: {ataque}\nDEFESA: {defesa}\n")
    continuar1=input("aperte qualquer tecla pra continuar")
class inimigo():
    monstro=random.randint(1,2)
    inimigo=boss(monstro)
    inimigo_nome,inimigo_classe,vida,ataque,defesa=inimigo.classes()
    print("Um monstro!!!\n")
    print(f"E um {inimigo_nome}\nCuidado ele e um {inimigo_classe}\n")
    continuar2=input("aperte qualquer tecla pra continuar")
class combate(ficha,inimigo):
    print(f"{inimigo.inimigo_nome} Voce e muito fraco vou deixar vc atacar primeiro!, hahaha...\n")
    turno=0
    
    
    while(ficha.vida>0 and inimigo.vida >0):

        turno+=1

        if turno %2!=0 :
           if(ficha.classe=="Mago"):
              print(f"{ficha.nome}-Fire boll!!\n")
              rolagem=random.randint(1,20)
              continuar=input("Aperte qualquer tecla para rolar o dado:\n")
              print(f"Mestre -Rolando dado...\n {rolagem}")
              if(rolagem>10):
                  print("Mestre -vc acertou!\n")
                  print(f"{inimigo.inimigo_nome} -Aagh..\n")
                  inimigo.vida+=-10
              elif(rolagem==1):
                  print("Mestre -FALHA CRITICA!\n vc tropeçou e perdeu 2 de vida\n")
                  ficha.vida+=-2
              
              else:
                  print("Mestre -vc Errou!\n")
                  print(f"{inimigo.inimigo_nome} -hahaha.. muito fraco\n")
           elif(ficha.classe=="Guerreiro"):
              print(f"{ficha.nome}-Sinta o gosto da minha lamina!!\n")
              rolagem=random.randint(1,20)
              continuar=input("Aperte qualquer tecla para rolar o dado:\n")
              print(f"Mestre -Rolando dado...\n {rolagem}")
              if(rolagem>10):
                  print("Mestre -vc acertou!\n")
                  print(f"{inimigo.inimigo_nome} -Aagh..\n")
                  inimigo.vida+=-10

              elif(rolagem==1):
                  print("Mestre -FALHA CRITICA!\n vc tropeçou e perdeu 2 de vida\n")
                  ficha.vida+=-2
              
              else:
                  print("Mestre -vc errou!\n")
                  print(f"{inimigo.inimigo_nome} -hahaha.. muito fraco\n")   
        else:
            if(inimigo.inimigo_nome=="Goblin"):
                 print(f"{inimigo.inimigo_nome}-Vou mostrar o poder dos Goblins Haaa!!\n")
                 rolagem=random.randint(1,20)
                 print(f"Mestre -Rolando dado...\n {rolagem}")
                 if(rolagem>10):
                  print("Mestre -O inimigo lhe acerta!\n")
                  print(f"{ficha.nome} -Aagh..\n")
                  ficha.vida+=-10
                  print(f"Sua vida hatual e: {ficha.vida}\n")
                 elif(rolagem==1):
                  print("Mestre -FALHA CRITICA!\n Ele tropeçou e perdeu vida\n")
                  inimigo.vida+=-2
                 else:
                  print("Mestre -O inimigo Erra!\n")
                  print(f"{ficha.nome} -hahaha.. muito fraco\n")
            elif(inimigo.inimigo_nome=="Bruxa"):
                 print(f"{inimigo.inimigo_nome}-Vou mostrar o poder de uma verdadeira bruxa Haaa!!\n")
                 print("Mestre -O inimigo lança uma esfera escura na nua direção e...")
                 rolagem=random.randint(1,20)
                 print(f"Mestre -Rolando dado...\n {rolagem}")
                 if(rolagem>10):
                  print("Mestre -O inimigo lhe acerta!\n")
                  print(f"{ficha.nome} -Aagh..\n")
                  ficha.vida+=-10
                  print(f"Sua vida hatual e: {ficha.vida}\n")
                 elif(rolagem==1):
                  print("Mestre -FALHA CRITICA!\n A magia flahae explode na mão dela, ela perdeu vida\n")
                  inimigo.vida+=-2
                 else:
                  print("Mestre -O inimigo Erra!\n")
                  print(f"{ficha.nome} -hahaha.. muito fraco\n")
        continuar=input("aperte qualquer tecla pra continuar")
        print(f"Fim do turno {turno}")
       

    print("Obrigado por jogar :)")    