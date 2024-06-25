h=float(input())
g=input()
t=float(input())
if g=='EARTH' :
    g = 9.8
elif g == 'MOON' :
    g = 1.6
elif g == 'JUPITER':
    g = 24.7
elif g == 'MARS' :
    g = 3.7
elif g == 'VENUS' :
    g = 8.8
elif g == 'ERIS' :
    g = 0.82

H= (g*t**2)/2

if H==h :
    print("MISSION COMPLETED.")
elif H>h :
    print("IT'S TOO SOON :(")
elif H<h :
    print("BOOOOOM!")

