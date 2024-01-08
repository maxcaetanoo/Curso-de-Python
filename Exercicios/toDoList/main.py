from Exercicios.toDoList.lib.archive import arqExists, arqCreate
from Exercicios.toDoList.lib.interface import menu

arq = 'list.txt'
if not arqExists(arq):
    arqCreate(arq)
menu(arq)
