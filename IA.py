#variaveis globais
NUMBER_MOVES = 15
NUMBER_GENES = 9
NUMBER_ORGANISMS = 15
MUTATION_RATE = 0.001
MAXIMUM_FITNESS = NUMBER_GENES
modelOrganism = [0,1,2,3,4,5,6,7,8]
geracao = []


from random import *

class Individuo:

    def __init__(self,numero,gene,fitness):
        self.id = numero
        self.gene = gene
        self.historico = []
        self.fitness = fitness


def movimento(individuo):
    branco = 0
    for i in range (0,NUMBER_GENES):
        if (individuo.gene[i]==0):
            branco = i
    for i in range (0,NUMBER_MOVES):
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
    #NUMBER_MOVES += 1

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

      InitializeOrganisms()

      #while(True):
        #perfectGeneration = EvaluateOrganisms()
        #if( perfectGeneration==True ):
        #    return generations
       # ProduceNextGeneration()
       # generations += 1

def Fitness(individuo):
    fitness = 0
    for gene in range (0,NUMBER_GENES):
        fitness += abs(individuo[gene]-gene)
    if (fitness == 0):
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
        movimento(geracao[organism])
        print(geracao[organism].gene)
        geracao[organism].fitness = Fitness(geracao[organism].gene)
        print("Valor fitness: ", geracao[organism].fitness,"\nID: ",geracao[organism].id)


    print("\nIndividuos com melhor fitness após movimentos\n")
    ordena_fitness(geracao)
    for organism in range(0,NUMBER_ORGANISMS):
        print(geracao[organism].gene)
        print("Valor fitness: ", geracao[organism].fitness,"\nID: ",geracao[organism].id,"\n")


DoOneRun()
