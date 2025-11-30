import numpy as np
import matplotlib.pyplot as plt

n=1000
N=100
T = 2
def MB():
    dT=T/N
    W=np.zeros(N)
    t=np.zeros(N)
    for i in range(N-1):
        W[i+1]=(W[i]+ np.sqrt(dT)* np.random.normal(0,1))
        t[i+1]=t[i]+dT
    plt.plot(t,W)
    return W
    # la fonction W est strictement croisant et donc le somme des difference est strictement croisant 
    # et pour deux point Wt et Ws, Wt-Ws est independant de tout point enclue entre ces deux points 

def plusieur_MB(n):
    for i in range(n):
        MB()
    plt.show()

def esperance_MB(n):
    last_value=[]
    last_value_abs=[]
    for i in range(n):
        last_value.append(MB()[N-1])
        last_value_abs.append(MB()[N-1]**2)
    esperance_MC_MB=np.mean(last_value)
    variance_MC_MB=np.mean(last_value_abs)-esperance_MC_MB**2
    print("espreance =",esperance_MC_MB," variance =",variance_MC_MB)

def verification_MC():
    somme = 0
    u=0.5
    for i in range(n):
        W=MB()[N-1]
        somme = somme + np.exp(u*W)
    resultat_MC = somme/n
    resultat_TH = np.exp(T*u**2/2)
    print("resultat_MC =",resultat_MC," resultat_TH =",resultat_TH)

def variation_quadratique():
    N=100
    Q = [0]
    t = [0]
    W = [0]

    dt = T/N
    for i in range(N):
        W.append(W[i]+ np.sqrt(dt)* np.random.normal(0,1))
        Q.append(Q[i]+(W[i+1]-W[i])**2)
        t.append(t[i]+dt)
        t[i+1]=t[i]+dt
    plt.plot(t,Q)
    plt.plot(t,t,'r')
    plt.show()

plusieur_MB(10)
esperance_MB(n)
verification_MC()
variation_quadratique()
