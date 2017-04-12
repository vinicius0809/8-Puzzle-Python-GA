#variaveis globais
NUMBER_MOVES = 100
NUMBER_GENES = 9
NUMBER_ORGANISMS = 10
MUTATION_RATE = 0.001
MAXIMUM_FITNESS = NUMBER_GENES
modelOrganism = [0,1,2,3,4,5,6,7,8]
geracao = []
ngeracao = 1


from random import *

class Individuo:

    def __init__(self,numero,gene,fitness):
        self.id = numero
        self.gene = gene
        self.historico = []
        self.fitness = fitness

def crossover(geracao):
    global ngeracao
    ngeracao +=1 
    novaGeracao = geracao[:]
    geracao = []
    for i in range (0,NUMBER_ORGANISMS):
        #fazer o crossover  entre os elementos de novaGeracao para inserir na nova lista geracao        
        geracao.append(Individuo(i*ngeracao,novaGeracao[i].gene,novaGeracao[i].fitness))
        novoHistorico = geracao[i].historico[:NUMBER_MOVES//2]
        geracao[i].historico = []
        geracao[i].historico = novoHistorico[:]
        movimento(geracao[i],NUMBER_MOVES//2, NUMBER_MOVES)

def movimento(individuo, inicio, fim):
    global NUMBER_MOVES
    branco = 0
    i = 0
    while(branco == 0):
        if(individuo.gene[i]==0):
            branco = i
        i+=1;
        
    for i in range (inicio,fim):
        sair = False
        while(not sair):
            sair = True
            aux = randint(0,4)
            if(aux==0 and move_direita(individuo,branco)):
                branco += 1
            elif(aux==1 and move_esquerda(individuo,branco)):
                branco -= 1
            elif(aux==2 and move_cima(individuo,branco)):
                branco -= 3
            elif(aux==3 and move_baixo(individuo,branco)):
                branco += 3
            else:
                sair = False
    
    NUMBER_MOVES += 1

def ordena_fitness(geracao):
    from operator import attrgetter
    geracao.sort(key=lambda a: a.fitness)


def move_direita(organism,i):
    if (i==0 or i==1 or i==3 or i==4 or i==6 or i==7):
        organism.gene[i],organism.gene[i+1] = organism.gene[i+1], organism.gene[i]
        organism.historico.append("Direita")
        return True
    return False


def move_esquerda(organism,i):
    if(i==2 or i==1 or i==5 or i==4 or i==8 or i==7):
        organism.gene[i],organism.gene[i-1] = organism.gene[i-1], organism.gene[i]
        organism.historico.append("Esquerda")
        return True
    return False


def move_baixo(organism,i):
    if (i==1 or i==4 or i==2 or i==5 or i==0 or i==3):
        organism.gene[i],organism.gene[i+3] = organism.gene[i+3], organism.gene[i]
        organism.historico.append("Baixo")
        return True
    return False

def move_cima(organism,i):
    if (i==7 or i==4 or i==3 or i==5 or i==6 or i==8):
        organism.gene[i],organism.gene[i-3] = organism.gene[i-3], organism.gene[i]
        organism.historico.append("Cima")
        return True
    return False

def DoOneRun():
      generations = 1;
      perfectGeneration = False

      print("\nIndividuos com melhor fitness após movimentos\n")
      ordena_fitness(geracao)
      for organism in range(0,NUMBER_ORGANISMS):
          print(geracao[organism].gene)
          print("Valor fitness: ", geracao[organism].fitness,"\nID: ",geracao[organism].id,'\n')
      crossover(geracao)
      print("\nIndividuos com melhor fitness após CROSSOVER\n")
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
            if (individuo[gene]==8):
                fitness+=4
            elif (individuo[gene]==5 or individuo[gene]==7):
                fitness+=3
            elif (individuo[gene]==1 or individuo[gene]==3):
                fitness+=1
            else:
                fitness+=2
        elif(gene==1):
            if (individuo[gene]==8 or individuo[gene]==6):
                fitness+=3
            elif (individuo[gene]==5 or individuo[gene]==7 or individuo[gene]==3):
                fitness+=2
            else:
                fitness+=1
        elif(gene==2):
            if (individuo[gene]==6):
                fitness+=4
            elif (individuo[gene]==3 or individuo[gene]==7):
                fitness+=3
            elif (individuo[gene]==1 or individuo[gene]==5):
                fitness+=1
            else:
                fitness+=2
        elif(gene==3):
            if (individuo[gene]==2 or individuo[gene]==8):
                fitness+=3
            elif (individuo[gene]==0 or individuo[gene]==4 or individuo[gene]==6):
                fitness+=1
            else:
                fitness+=2
        elif(gene==4):
            if (individuo[gene]==1 or individuo[gene]==3 or individuo[gene]==5 or individuo[gene]==7):
                fitness+=1
            else:
                fitness+=2
        elif(gene==5):
            if (individuo[gene]==0 or individuo[gene]==6):
                fitness+=3
            elif (individuo[gene]==2 or individuo[gene]==4 or individuo[gene]==8):
                fitness+=1
            else:
                fitness+=2
        if(gene==6):
            if (individuo[gene]==2):
                fitness+=4
            elif (individuo[gene]==5 or individuo[gene]==1):
                fitness+=3
            elif (individuo[gene]==7 or individuo[gene]==3):
                fitness+=1
            else:
                fitness+=2
        elif(gene==7):
            if (individuo[gene]==0 or individuo[gene]==2):
                fitness+=3
            elif (individuo[gene]==1 or individuo[gene]==5 or individuo[gene]==3):
                fitness+=2
            else:
                fitness+=1
        else:
            if (individuo[gene]==0):
                fitness+=4
            elif (individuo[gene]==1 or individuo[gene]==3):
                fitness+=3
            elif (individuo[gene]==7 or individuo[gene]==5):
                fitness+=1
            else:
                fitness+=2
            
    if (fitness <= 20):
        print("Sequencia para resolver: ",individuo.historico)
    return fitness

def InitializeOrganisms():
    vet_comparacao = []
    for aux in range (0,NUMBER_GENES):
        vet_comparacao.append (False)

    print("Disposicao inicial: ")
    inicialModel = []
    for gene in range (0,NUMBER_GENES):
        i=True
        while (i==True):
            aux = randint(0,8)
            if(vet_comparacao[aux]==False):
                vet_comparacao[aux] = True
                inicialModel.append(aux)
                i=False
    for x in range (0,NUMBER_ORGANISMS):
        copiaInicialModel = inicialModel[:]
        geracao.append(Individuo(x,copiaInicialModel,0))

    print(inicialModel[0:NUMBER_GENES])
    print(modelOrganism[0:NUMBER_GENES])
    print("Valor do fitness inicial: ",Fitness(inicialModel))

    print("\nIndividuos após movimentos\n")
    for organism in range(0,NUMBER_ORGANISMS):
        movimento(geracao[organism],0,NUMBER_MOVES)
        print(geracao[organism].gene)
        geracao[organism].fitness = Fitness(geracao[organism].gene)
        print("Valor fitness: ", geracao[organism].fitness,"Melhoria: ",Fitness(inicialModel)-geracao[organism].fitness,"\nID: ",geracao[organism].id)


InitializeOrganisms()
while(True):
    DoOneRun()


