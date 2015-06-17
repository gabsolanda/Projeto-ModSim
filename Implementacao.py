# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:38:18 2015

@author: Gabriel Olanda
"""
from Angulos import RetornaAngulos
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
import math

Ang = RetornaAngulos()

m = 70 # Kg
g = 9.8 # m/s²
k = 0.47 * 0.5 * 
l = 6 # m

def func(v,T):
    dWdt = v[1]
    dAdt = (m * g * math.sin(math.radians(v[0])) - k * (l)**2 * O[1] * (((O[1])**2)**0.5))/ (m * l)
    
    return [dWdt, dAdt]
    
w0 = 0 # m/s
a0 = 9.8 # m/s²

V0 = [w0, a0]

T = linspace(0,12,12)

Ac = odeint(func, V0, T)

print(Ac)

plt.plot(T, Ac[:,1])
plt.axis([0, max(T), 0, 20])
plt.ylabel('y')
plt.xlabel('t')
plt.show()