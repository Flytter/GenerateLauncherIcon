from lib.getItensFromEntrance import *
import os


class controllerImg:
    
    def __init__(self, path):
        self.itens = getItens()
        self.listItens = getItens().getFile(path)

    def resizeImage(self):
        for i in self.listItens:
            print(i)


