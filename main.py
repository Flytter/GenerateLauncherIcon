from lib.getItensFromEntrance import getItens
from lib.controllerImage import controllerImg
import os


pathDirect = os.getcwd()

resizeImage = controllerImg(pathDirect)
resizeImage.resizeImage()
