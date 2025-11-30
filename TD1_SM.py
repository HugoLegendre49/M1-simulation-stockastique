import numpy as np
import matplotlib.pyplot as plt
import random

#def de l'arbre fait avec la prof

#parametres :

def modele_binomial():
    #parametre :
    T=0.5
    r=0.1
    s0=10
    N=20
    K=200

    lamda = 0.5
    t=T/N

    u= np.exp(lamda*np.sqrt(t))
    d= np.exp(-lamda*np.sqrt(t))
    p=(np.exp(r*t)-d)/(u-d)
    #arbre

    t=np.linspace(0,T,N+1)
    s=np.zeros((N+1,N+1))
    for n in range(N+1):
        for a in range(n+1):
            s[n,a]=s0*(u**a)*(d**(n-a))
    plt.plot(t,s,'*')

    #simulation de marche aleatoire :
    Smc=np.zeros(N+1)
    esperance=np.zeros(N+1)
    Smc[0]=s0
    esperance[0]=K*s0
    for a in range(K):
        for n in range(N):
            if random.random() <= p:
                Smc[n+1]=u*Smc[n]
                esperance[n+1]=esperance[n+1]+Smc[n+1]
            else:
                Smc[n+1]=d*Smc[n]
                esperance[n+1]=esperance[n+1]+Smc[n+1]
        plt.plot(t,Smc)
    
    #affichage et calcul d'esperence : 
    for a in range(N+1):
        esperance[a]=esperance[a]/K
    plt.plot(t,esperance,'r',linewidth=3, label='esperance')
    plt.legend()
    plt.title("Simulation de marche aléatoire")
    plt.show()
    esperance_r = s0*(p*u+d*(1-p))**N
    print("esperance finale:",esperance[N], "esperence réel = ", esperance_r, "difference", np.abs(esperance[N]-esperance_r))

#modele_binomial()

def martingale(debug = False):
    #variable :

    N= 20
    K = 10
    T= 1
    W= 1000
    M= np.zeros(N+1)
    esperance = np.zeros(N+1)
    esperance[0]= M[0]*W
    # creation des poinds

    t=np.linspace(0,T,N+1)
    s=np.zeros((N+1,N+1))
    for n in range(N+1):
        for a in range(n+1):
            s[n,a]=M[0]+(a)-((n-a))
    plt.plot(t,s,'*')
    # creation du trons

    for a in range(1,K+1):
        if random.random()<=0.5:
            M[a]=M[a-1]+1
        else:
            M[a]=M[a-1]-1
        esperance[a]=M[a]
        
    #creation des branche :


    for a in range(W):
        for a in range(K+1,N+1):
            if random.random()<=0.5:
                M[a]=M[a-1]+1
            else:
                M[a]=M[a-1]-1
        if debug:
            print(len(M), len(t))
        plt.plot(t,M)
    plt.show()

martingale()
