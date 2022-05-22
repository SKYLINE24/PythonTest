pi = 3.14
yariCap= int(input("yarı çap giriniz:"))
alan= pi * (yariCap**2)
cevre= 2* pi * yariCap
"""
bu şekilde yazmazsak aşşadaki gibi yazmalıyız
print("alan",alan)
print("çevre",cevre)
"""
print("alan" + str(alan) + "  cevre" + str(cevre))