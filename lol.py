print("--------------------------------------")#bienvenida al usuario
print("    B I E N V E N I D O")
print("--------------------------------------")
papacr=6000#precios de los productos
papapast=4000#precios de los productos
namcr=("1) PAPA CRIOLLA")# producto 1
nampas=("2) PAPA PASTUSA")# producto 2
mis_productos=()
lal=()
lol=()
m=()
n=()
print(" MENU DE PRODUCTOS")#

print(namcr)
print(nampas)#

print("=====================================")
xd=True
while xd:
    wvw=input("\nESCOJA QUE TIPO DE PAPA DESEA COMPRAR\n")
    if wvw==1:
     lol=int(input("\ncuantas papas vas a llevar\n"))
     n=lol*papacr
     print("   lista de compra")
     mis_productos=(namcr,lol,n)
     print(mis_productos)
            
    if wvw==2:
     lal=int(input("\ncuantas papas vas a llevar\n"))
     m=lal*papapast
     print("   lista de compra")
     mis_productos(nampas,lal,m)
     print(mis_productos)
xd=False

 