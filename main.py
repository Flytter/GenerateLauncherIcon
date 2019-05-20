from lib.getItensFromEntrance import getItens
from lib.controllerImage import controllerImg
import os
import sys


arguments = sys.argv
pathDirect = os.getcwd()

resizeImage = controllerImg(pathDirect, arguments)
resizeImage.resizeImage()
