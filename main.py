from testare.teste import Teste
from coordonare.appCoord import AppCoord

if __name__=='__main__':
    teste = Teste()
    teste.ruleaza_teste()
    appCoord = AppCoord()
    appCoord.start()