from Exercicios.toDoList.lib import interface, classes, archive

arq = 'to_do_list.txt'
if not archive.arqExists(arq):
    archive.arqCreate(arq)
interface.menu(arq)
