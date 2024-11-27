A=int(input("Cuantos metros cuadrados se necesitan para producir un litro de leche "))
M=int(input("Cuantos metros cuadrados tiene el corral "))
V=int(input("Cuantas vacas tiene el corral "))
litro_dia=M/A
Total=(V*litro_dia)*7
print(f"{V} Vacas producen {Total} litros de leche ")




aves=int(input("Cuantas aves tiene el galpon "))
gall=aves/3
mg=gall/2
mg1=mg*(30/3)
mg2=mg*(30/5)
mgt=mg1+mg2
print(f"en un mes producen {mgt} huevos mensuales")