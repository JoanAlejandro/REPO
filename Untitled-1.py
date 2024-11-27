A=int(input("Cuantos metros cuadrados se necesitan para producir un litro de leche "))
M=int(input("Cuantos metros cuadrados tiene el corral "))
V=int(input("Cuantas vacas tiene el corral "))
litro_dia=M/A
Total=(V*litro_dia)*7
print(f"{V} Vacas producen {Total} litros de leche ")