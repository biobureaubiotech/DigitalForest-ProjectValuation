import random
import numpy
import matplotlib.pyplot as plt

def custo(numamostras):
    global custototal
    defidcol = random.randint(500,1000) #chute
    ext = random.randint(180,400) #extração etanólica (orçamentosenai,chute)
    abio = random.randint(40,900) #(orçamentoMTK,orçamentoGSS)
    custototal = numamostras*(defidcol + ext + abio)
    #print('O custo total foi R$%i.00 considerando um valor para definição, identificação e coleta de R$%i.00, para extratos de R$%i.00 e para acesso a bioversidade de R$%i.00.' %(custototal, defidcol, ext, abio))

n = 1000000
numamostras = 1000
i=0
listacusto = []

while i < n:
    custo(numamostras) #custo para numamostras = 1000
    listacusto.append(custototal)
    i+=1

print('Após {:,} simulações: \
        \n custo médio: R${:,.2f} \
        \n coeficiente de variação: {:.0f}% \
        \n menor custo calculado: R${:,.2f} \
        \n e o maior: R${:,.2f}.\
        \n Pode-se afirmar com 95% de certeza que o custo total para produção de {} extratos está entre R${:,.2f} e R${:,.2f}.'\
      .format(n, numpy.mean(listacusto), (numpy.std(listacusto)/numpy.mean(listacusto))*100, min(listacusto), max(listacusto), numamostras, numpy.mean(listacusto)-2*numpy.std(listacusto), numpy.mean(listacusto)+2*numpy.std(listacusto)))
    
plt.hist(listacusto, normed=0, bins=50) #normed=0 mostra as frequências, normed=1 as probabilidades (integral da curva fica 1)
plt.xlabel('Custo Total')
plt.ylabel('Frequência')
plt.title('Histograma do Custo Total')
plt.show()
