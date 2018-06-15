# Esse script é útil para avaliar a volatilidade no fluxo de caixa de 1 ano do projeto

import random
import numpy
#import matplotlib.pyplot as plt

# calculando o custo para a produção de um número de extratos para 1 cenário
def Custo(NumAmostras):
    DefIdCol = random.randint(500,1000)             # definição + identificação + coleta chute (phytobios)
    Extracao = random.randint(120,180)              # extração etanólica (orçamento IPPN, orçamentosenai)
    AcessoBiodiv = random.randint(40,900)           # (orçamentoMTK,orçamentoGSS)
    CustoTotal = NumAmostras*(DefIdCol + Extracao + AcessoBiodiv)
    return CustoTotal

def CustoMedioEstocatico(NumAmostras, NumSimulacoes):         # numsimulacoes > 10.000
    listacusto = []
    for i in range(0,NumSimulacoes):                      
        listacusto.append(Custo(NumAmostras))
    CustoMedio = numpy.mean(listacusto)
    return CustoMedio

# calculando a receita para 1 do projeto
def ReceitaProjetos():
    NumProjetos = random.randint(0,30)                                  # chute
    NumExtratosPorProjeto = random.choice([32, 32, 32, 128])            # HTS de 96 e 384 (1536 não considerado) poços com testes em triplicata                       
    if NumExtratosPorProjeto == 32:
        ReceitaPorExtrato = 1800
    else:
        ReceitaPorExtrato = 1400
    Receita = NumProjetos*NumExtratosPorProjeto*ReceitaPorExtrato
    return Receita

def ReceitaMediaEstocatica(NumSimulacoes):
    listareceita = []
    for i in range(0,NumSimulacoes):                     
        listareceita.append(ReceitaProjetos())
    ReceitaMedia = numpy.mean(listareceita)
    return ReceitaMedia

def SaldoMedioEstocatico(NumAmostras, n):         # numsimulacoes > 10.000
    global SaldoMedio, DesvioPadrao
    listasaldo = []
    for i in range(0,n):                     
        Saldo = ReceitaMediaEstocatica(100) - CustoMedioEstocatico(1000,100)
        listasaldo.append(Saldo)
    SaldoMedio = numpy.mean(listasaldo)
    DesvioPadrao = numpy.std(listasaldo)
    #plt.hist(listasaldo, normed=0, bins=50)         #normed=0 mostra as frequências, normed=1 as probabilidades (integral da curva fica 1)
    #plt.show()


# chamando as funções
SaldoMedioEstocatico(1000, 1000)
print('R${:,.2f} com desvio de R${:,.2f} ou {:,.2f}%'.format(SaldoMedio, DesvioPadrao, abs(DesvioPadrao/SaldoMedio*100)))
 
