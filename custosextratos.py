import random
import numpy

def custo():
    global custototal
    global defidcol
    global ext
    global abio
    
    numamostras = 600
    defidcol = random.randint(300,1000) #chute orçamento phytobios R$1000,00 expedição + extrato
    ext = random.randint(180,500) #extração etanólica (orçamentosenai,chute)
    abio = random.randint(40,900) #(orçamentoMTK,orçamentoGSS)
    custototal = numamostras*(defidcol + ext + abio)
    #print('O custo total foi R$%i.00 considerando um valor para definição, identificação e coleta de R$%i.00, para extratos de R$%i.00 e para acesso a bioversidade de R$%i.00.' %(custototal, defidcol, ext, abio))

i=0
listacusto = []
listadefidcol = []
listaext = []
listaabio = []

while i < 100000:
    custo()
    listacusto.append(custototal)
    listadefidcol.append(defidcol)
    listaext.append(ext)
    listaabio.append(abio)
    i+=1

#print(listacusto)
print(numpy.mean(listacusto))
#print(numpy.std(listacusto))
print((numpy.std(listacusto)/ numpy.mean(listacusto))*100) #coeficiente de variação (desvio padrão relativo)
print(min(listacusto))
print(max(listacusto))
#print('###')
#print(numpy.mean(listadefidcol))
#print((numpy.std(listadefidcol/ numpy.mean(listadefidcol))*100))
#print('###')
#print(numpy.mean(listaext))
#print((numpy.std(listaext)/ numpy.mean(listaext))*100) 
#print('###')
#print(numpy.mean(listaabio))
#print((numpy.std(listaabio/ numpy.mean(listaabio))*100)) 
