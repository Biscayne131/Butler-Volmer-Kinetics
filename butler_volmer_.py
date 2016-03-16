# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:17:24 2016

@author: Can_
"""

def butler_volmer(alpha,knot,conc,Enot,E):
    
    """Making sure alpha is valid"""
    
    if alpha>1 or alpha<0: 
        print 'Enter 0<=alpha<=1'
        return 
    F=96485.3
    f=F/(8.3145*298.15)
    import numpy as np
    
    """ Plotting functions are added but silenced for clarity """
    
    """import matplotlib.pyplot as plt"""
    
    """Creating the potential space"""
    
    ptntl=np.linspace(0,1,num=10000)*E 
    nu=np.array(ptntl-Enot)
    
    """This is actually the current density on electrode surface since we do
    not multiply by area but it would not make a huge difference and would be 
    pretty easy to implement another variable to the function regarding area"""
    
    inot=F*knot*conc
    icat=np.array((np.exp(alpha*f*nu))*inot)
    iano=np.array((np.exp((1-alpha)*f*nu))*inot)
    
    """Flipping the anodic current to fit a convention; anodic(positive)
    potentials to the right with negative current"""
    
    iano2=iano[::-1]
    inet=icat-iano2

    """
    plt.plot(-ptntl,inet)
    plt.show()
    """
    tafelnet=np.array(np.log(np.abs(inet)))
    
    """Similarly the tafel plot is with the same convention, the curve on the
    right side of the plot is anodic"""
    
    """
    plt.plot(-nu,tafelnet)
    plt.show()
    """
    
    """The function returns the relevant information"""
    
    return(inet,tafelnet,nu,ptntl)
    
"""Examples"""

z=0
alpha=[0.5,0.4,0.3]
import matplotlib.pyplot as plt
for z in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(alpha[z],1e-7,10e-6,0.2444,0.9)
    plt.plot(-ptntl,inet)
    z=z+1
plt.show()

""" Tafel plot"""

m=0
import matplotlib.pyplot as plt
for m in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(alpha[m],1e-7,10e-6,0.2444,0.9)
    plt.plot(-ptntl,tafelnet)
    m=m+1
plt.show()


del z
knot=[10e-7,10e-6,10e-7]
alpha=[0.50,0.50,0.55]
for z in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(alpha[z],knot[z],10e-6,0.2444,0.9)
    plt.plot(-ptntl,inet)
    z=z+1
plt.show()
del m


for m in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(alpha[m],knot[m],10e-6,0.2444,0.9)
    plt.plot(-ptntl,tafelnet)
    m=m+1
plt.show()

del z,knot
knot=[10e-9,10e-9,10e-7]
enot=[0.2,0.1,0.2]
for z in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(0.5,knot[z],10e-6,enot[z],0.9)
    plt.plot(-ptntl,inet)
    z=z+1
plt.show()


del m
for m in range(3):
    [inet,tafelnet,nu,ptntl]=butler_volmer(0.5,knot[m],10e-6,enot[m],0.9)
    plt.plot(-ptntl,tafelnet)
    m=m+1
plt.show()

