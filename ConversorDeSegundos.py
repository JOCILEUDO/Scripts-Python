TotalDeSeg_str = input("Digite os segundos que deseja converter: ")
TotalSegundos = int(TotalDeSeg_str)

# Convertendo os segundos
Dias = TotalSegundos //(3600*24)
SegRestantes = TotalSegundos %(3600*24)

Horas = SegRestantes //3600
SegRestantes = SegRestantes %3600

Minutos = SegRestantes //60

Segundos = SegRestantes %60

print(TotalSegundos,"segundos equivale a: ",Dias, " Dias ",Horas," Horas ", Minutos," Minutos e ", Segundos," Segundos.")