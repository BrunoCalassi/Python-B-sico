from pathlib import Path
#Absolute Path
#Relative Path

#path=Path('email')# ditretorio especifico
#print(path.exists()) #verifica s diretorio existe
#print(path.mkdir()) #cria diretorio
#print(path.rmdir()) #remove diretorio

path=Path() #nesse diretorio
for file in path.glob('*'): #todos as pastas   /   ('*.py') arquivos py  nesse diretorio
    print(file)