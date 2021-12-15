weight = input("Weight: ")
def pounds(poud, wegt):
    return poud*wegt
def kilo(kio, wht):
    return wht/kio
q_kilo_pound = input("L(lbs) or K(kilo): ")
if q_kilo_pound.lower() == "l":
    result = pounds(0.45, int(weight))
elif q_kilo_pound.lower() == "k":
    result = kilo(int(weight), 0.45)
print (result)
