"""De la tastaura se introduce numarul de rand al culorii curcubeului.
De afisat denumirea culorii.Convenim ca culoarea rosie are numareul de rand 1"""
n=int(input("dati numarul culorii:"))
if n==1:
    print("rosu")
if n==2:
    print("oranj")
if n==3:
    print("galben")
if n==4:
    print("ver4de")
if n==5:
    print("albastru")
if n==6:
    print("indigo")
if n==7:
    print("violet")
if (n>7) or (n<1):
    print("curcubeul are 7 culori")