#variaveis globais
NUMBER_MOVES = 1
NUMBER_GENES = 9
NUMBER_ORGANISMS = 50
MUTATION_RATE = 0.001
modelOrganism = [0,1,2,3,4,5,6,7,8]
geracao = []
ngeracao = 1


from random import *

class Individuo:

    def __init__(self,numero,gene,fitness):
        self.id = numero
        self.gene = gene
        self.historico = ["Inicio"]
        self.fitness = fitness

def crossover(geracao):
    global NUMBER_MOVES
    NUMBER_MOVES += 1
    aux = NUMBER_MOVES
    global ngeracao
    ngeracao +=1
    novaGeracao = geracao[:]
    geracao = []
    for i in range (0,NUMBER_ORGANISMS):
        #fazer o crossover  entre os elementos de novaGeracao para inserir na nova lista geracao
        geracao.append(Individuo((i+1)*ngeracao,novaGeracao[i].gene,0))
        novoHistorico = novaGeracao[i].historico[:(NUMBER_MOVES-1)]
        geracao[i].historico = []
        geracao[i].historico = novoHistorico[:]
        movimento(geracao[i],(NUMBER_MOVES-1),(NUMBER_MOVES))
        geracao[i].fitness = Fitness(geracao[i])
    return geracao


def movimento(individuo, inicio, fim):
    branco = -1
    i = 0
    while(branco == -1):
        if(individuo.gene[i]==0):
            branco = i
        i+=1;

    for i in range (inicio,fim):
        sair = False
        while(not sair):
            sair = True
            aux = randint(0,4)
            if(aux ==0 and individuo.historico[-1] != 'Esquerda' and move_direita(individuo,branco,individuo.fitness)) :
                branco += 1
            elif(aux ==1 and individuo.historico[-1] !='Direita'and move_esquerda(individuo,branco,individuo.fitness)):
                branco -= 1
            elif(aux ==2 and individuo.historico[-1] != 'Baixo' and move_cima(individuo,branco,individuo.fitness)):
                branco -= 3
            elif(aux ==3 and individuo.historico[-1] != 'Cima' and move_baixo(individuo,branco,individuo.fitness)):
                branco += 3
            else:
                sair = False


def ordena_fitness(geracao):
    from operator import attrgetter
    geracao.sort(key=lambda a: a.fitness)

def media_fitness(geracao):
    media_geracao = 0
    for i in range (0,NUMBER_ORGANISMS):
        media_geracao += geracao[i].fitness
    return media_geracao/NUMBER_ORGANISMS

def move_direita(organism,i,fitness_atual):
    if (i==0 or i==1 or i==3 or i==4 or i==6 or i==7):
        organism.gene[i],organism.gene[i+1] = organism.gene[i+1], organism.gene[i]
        organism.historico.append("Direita")
        return True
    return False


def move_esquerda(organism,i,fitness_atual):
    if(i==2 or i==1 or i==5 or i==4 or i==8 or i==7):
        organism.gene[i],organism.gene[i-1] = organism.gene[i-1], organism.gene[i]
        organism.historico.append("Esquerda")
        return True
    return False


def move_baixo(organism,i,fitness_atual):
    if (i==1 or i==4 or i==2 or i==5 or i==0 or i==3):
        organism.gene[i],organism.gene[i+3] = organism.gene[i+3], organism.gene[i]
        organism.historico.append("Baixo")
        return True
    return False

def move_cima(organism,i,fitness_atual):
    if (i==7 or i==4 or i==3 or i==5 or i==6 or i==8):
        organism.gene[i],organism.gene[i-3] = organism.gene[i-3], organism.gene[i]
        organism.historico.append("Cima")
        return True
    return False

def DoOneRun():
      global geracao
      generations = 1;
      perfectGeneration = False

      print("\nMedia Fitness geracao anterior: ",media_fitness(geracao),"\nIndividuos com melhor fitness após CROSSOVER\n")
      geracao = crossover(geracao)
      ordena_fitness(geracao)
      for organism in range(0,NUMBER_ORGANISMS):
          print(geracao[organism].gene)
          print("Valor fitness: ", geracao[organism].fitness,"\nID: ",geracao[organism].id,'\n')

      #while(True):
        #perfectGeneration = EvaluateOrganisms()
        #if( perfectGeneration==True ):
        #    return generations
       # ProduceNextGeneration()
       # generations += 1

def Fitness(individuo):
    fitness = 0
    for gene in range (0,NUMBER_GENES):
        if(gene==0):
            if (individuo.gene[gene]==8):
                fitness+=4
            elif (individuo.gene[gene]==5 or individuo.gene[gene]==7):
                fitness+=3
            elif (individuo.gene[gene]==1 or individuo.gene[gene]==3):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==1):
            if (individuo.gene[gene]==8 or individuo.gene[gene]==6):
                fitness+=3
            elif (individuo.gene[gene]==5 or individuo.gene[gene]==7 or individuo.gene[gene]==3):
                fitness+=2
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=1
        elif(gene==2):
            if (individuo.gene[gene]==6):
                fitness+=4
            elif (individuo.gene[gene]==3 or individuo.gene[gene]==7):
                fitness+=3
            elif (individuo.gene[gene]==1 or individuo.gene[gene]==5):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==3):
            if (individuo.gene[gene]==2 or individuo.gene[gene]==8):
                fitness+=3
            elif (individuo.gene[gene]==0 or individuo.gene[gene]==4 or individuo.gene[gene]==6):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==4):
            if (individuo.gene[gene]==1 or individuo.gene[gene]==3 or individuo.gene[gene]==5 or individuo.gene[gene]==7):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==5):
            if (individuo.gene[gene]==0 or individuo.gene[gene]==6):
                fitness+=3
            elif (individuo.gene[gene]==2 or individuo.gene[gene]==4 or individuo.gene[gene]==8):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==6):
            if (individuo.gene[gene]==2):
                fitness+=4
            elif (individuo.gene[gene]==5 or individuo.gene[gene]==1):
                fitness+=3
            elif (individuo.gene[gene]==7 or individuo.gene[gene]==3):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2
        elif(gene==7):
            if (individuo.gene[gene]==0 or individuo.gene[gene]==2):
                fitness+=3
            elif (individuo.gene[gene]==1 or individuo.gene[gene]==5 or individuo.gene[gene]==3):
                fitness+=2
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=1
        else:
            if (individuo.gene[gene]==0):
                fitness+=4
            elif (individuo.gene[gene]==1 or individuo.gene[gene]==3):
                fitness+=3
            elif (individuo.gene[gene]==7 or individuo.gene[gene]==5):
                fitness+=1
            elif (individuo.gene[gene]==gene):
                fitness+=0
            else:
                fitness+=2

    individuo.fitness = fitness

    if (fitness == 0):
        print(individuo.gene,"Fitness individuo: ", individuo.fitness, "ID: ", individuo.id)
        print("Sequencia para resolver: ",individuo.historico)
        print("Programa acabou na geracao",NUMBER_MOVES)
        input("---")

    return individuo.fitness

def InitializeOrganisms():
    vet_comparacao = []
    for aux in range (0,NUMBER_GENES):
        vet_comparacao.append (False)

    print("Disposicao inicial: ")
    inicialModel = Individuo(0,[],0)
    for gene in range (0,NUMBER_GENES):
        i=True
        while (i==True):
            aux = randint(0,8)
            if(vet_comparacao[aux]==False):
                vet_comparacao[aux] = True
                inicialModel.gene.append(aux)
                i=False
    for x in range (0,NUMBER_ORGANISMS):
        copiaInicialModel = inicialModel.gene[:]
        geracao.append(Individuo(x+1,copiaInicialModel,0))

    print(inicialModel.gene[0:NUMBER_GENES])
    print(modelOrganism[0:NUMBER_GENES])
    print("Valor do fitness inicial: ",Fitness(inicialModel))

    print("\nIndividuos após",NUMBER_MOVES,"movimentos\n")
    for organism in range(0,NUMBER_ORGANISMS):
        movimento(geracao[organism],0,NUMBER_MOVES)
        print(geracao[organism].gene)
        geracao[organism].fitness = Fitness(geracao[organism])
        print("Valor fitness: ", geracao[organism].fitness,"Melhoria: ",Fitness(inicialModel)-geracao[organism].fitness,"\nID: ",geracao[organism].id)


InitializeOrganisms()
while(True):
    DoOneRun()
    print("\nNUMBER_MOVES =", NUMBER_MOVES)
