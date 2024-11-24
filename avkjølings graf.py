import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = open("Data.txt","r")
temp = []
tid = []
for line in data:
    parts = line.strip().split()
    if len(parts) == 2:
        tid.append(float(parts[0]))
        temp.append(float(parts[1]))
data.close()


temp = np.array(temp)
tid = np.array(tid)
Tk = 22.4
T0 = temp[0]
def T(t,a):
    return Tk+(T0-Tk)*np.exp(-a*t)

popt, _ = curve_fit(T, tid, temp)
alpha = popt[0]

Ttemp = T(tid,alpha)

plt.plot(tid,Ttemp, color="g", label = "Teoretisk data")
plt.plot(tid,temp,marker ="o",color="r", label = "målte data")
plt.xlabel("tid(min)")
plt.ylabel("temperatur(°C)")
plt.legend()
plt.grid()
plt.show()
print(f"Alpha ={round(alpha,5)}")



