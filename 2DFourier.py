import os
from math import e, pi, sin, cos

# the fft and ifft functions compute the DFT and inverse DFT, respectively.
from lib6300.fft import fft, ifft, ifft2, fft2
from lib6300.image import png_write

def G(Omega_r, Omega_c, W_r, W_c, r_0, c_0):

    firstpart = e**(-1j*r_0*Omega_r)
    thirdpart= e**(-1j*c_0*Omega_c)

    secondpart = W_r
    if (Omega_r != 0):
        secondpart = (1-e**(-1j*Omega_r*W_r))/(1-e**(-1j*Omega_r))

    fourthpart = W_c
    if (Omega_c != 0):
        fourthpart =  (1-e**(-1j*Omega_c*W_c))/(1-e**(-1j*Omega_c))

    return firstpart * secondpart * thirdpart * fourthpart

def M(Omega_r, Omega_c):

    onem = G(Omega_r,Omega_c,11,2,1,1)
    secondm = G(Omega_r,Omega_c,8,2,1,4)
    thirdm = G(Omega_r,Omega_c,11,2,1,7)

    onei = G(Omega_r,Omega_c,2,2,1,10)
    secondi = G(Omega_r,Omega_c,8,2,4,10)

    onet = G(Omega_r,Omega_c,2,7,1,13)
    secondt = G(Omega_r,Omega_c,8,2,4,13)

    return onem+secondm+thirdm+onei+secondi+onet+secondt


imagedft = []
for r in range(13):
    accessory = []
    for c in range(21):
        accessory.append(M(2*pi*r/13,2*pi*c/21))
    imagedft.append(accessory)

png_write(ifft2(imagedft), "m1a.png", zero_loc = 'topleft')
    


imagedft2 = []
for r in range(26):
    accessory2 = []
    for c in range(42):
        accessory2.append(M(2*pi*r/26,2*pi*c/42))
    imagedft2.append(accessory2)

png_write(ifft2(imagedft2), "m1apartb.png", zero_loc = 'topleft')






