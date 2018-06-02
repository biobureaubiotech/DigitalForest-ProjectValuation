import random
import numpy

def custo():
    global custototal
    
    numamostras = 1000
    defidcol = random.randint(300,1000) #chute
    ext = random.randint(180,500) #extração etanólica (orçamentosenai,chute)
    abio = random.randint(40,900) #(orçamentoMTK,orçamentoGSS)
    custototal = numamostras*(defidcol + ext + abio)
    #print('O custo total foi R$%i.00 considerando um valor para definição, identificação e coleta de R$%i.00, para extratos de R$%i.00 e para acesso a bioversidade de R$%i.00.' %(custototal, defidcol, ext, abio))

n = 100000
i=0
listacusto = []

while i < n:
    custo()
    listacusto.append(custototal)
    i+=1

print('Após {:,} simulações: \
        \n custo médio: R${:,.2f} \
        \n coeficiente de variação: {:.0f}% \
        \n menor custo calculado: R${:,.2f} \
        \n e o maior: R${:,.2f}.' \
      .format(n, numpy.mean(listacusto), (numpy.std(listacusto)/numpy.mean(listacusto))*100, min(listacusto), max(listacusto)))
