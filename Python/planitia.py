import re

dados = []
title = "latitudeGrau;latitudeMinuto;latitudeSegundo;latitudeMilissegundo;longitudeGrau;longitudeMinuto;longitudeSegundo;longitudeMilissegundo\n"

try:
    regex = r'''(L\s*o\s*n\s*g\s*i\s*t\s*u\s*d\s*e\s*:\s* [-]?\s*\d\s*\d\s*°\s*\d\s*\d\s*'\s*\d\s*\d\s*,\s*\d\s*\d\s*\d\s*\"\s*,\s* L\s*a\s*t\s*i\s*t\s*u\s*d\s*e:\s* [-]?\d\s*\d\s*°\s*\d\s*\d\s*'\s*\d\s*\d\s*,\s*\d\s*\d\s*\d\s*\"\s*)'''
    pathArquivo = input("Digite o nome do arquivo com extensão: ")
    file = open(pathArquivo, "rt")
    arquivo = file.read()
    
    file.close()
    
    arquivo = re.sub(r"Â", "", arquivo)
    match = re.findall(regex, arquivo)

    for element in match:
        element.replace("\n", "")
        grau = re.findall((r"(.[0-9]*)°"), element)
        minuto = re.findall((r"((?!°).\s*[0-9]*)'(?!')"), element)
        segundo = re.findall((r"'(.\s*[0-9])"), element)
        milissegundo = re.findall((r",(.\s*[0-9]\s*\d)"), element)
        dados.append(str(grau[0].replace("\n", "")) + ";" + str(minuto[0].replace("\n", "")) + ";" + str(segundo[0].replace("\n", "")) + ";" + str(milissegundo[0].replace("\n", "")) + ";" + str(grau[1].replace("\n", "")) + ";" + str(minuto[1].replace("\n", "")) + ";" + str(segundo[1].replace("\n", "")) + ";" + str(milissegundo[1].replace("\n", "")) + "\n")   
          
    csv = open("coordenadas.csv", "w")
    csv.writelines(title)
    
    for dado in dados:
        csv.writelines(dado)
        
    csv.close()
    print('Finalizado!')
   
except Exception as ex:
    print(ex)


input()

