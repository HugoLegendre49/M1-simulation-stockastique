#parametre :
import numpy as np
import matplotlib.pyplot as plt
N = 1000
Nmc = 1000
T = 10
dt = T/N
# travail 1 solution de l'intégrale
def Theta(t,x):
    return x

def integrale ():
    W = np.zeros(N+1)
    I = np.zeros(N+1)
    for i in range(N):
        t = i*dt
        W[i+1] = W[i] + np.sqrt(dt)*np.random.normal(0,1)
        I[i+1] = I[i] + Theta(t,W[i])* (W[i+1]-W[i])
    return I[N]

def I_mc():
    S = 0
    for j in range(Nmc):
        S += integrale()
    return S/Nmc

print("La valeur de l'intégrale stochastique est :", I_mc())

#travail 2 on verifie Wt² - 0 = 2*∫Ws dWs + t

def verif ():
    W = np.zeros(N+1)
    I = np.zeros(N+1)
    for i in range(N):
        W[i+1] = W[i] + np.sqrt(dt)*np.random.normal(0,1)
        I[i+1] = I[i] + W[i]* (W[i+1]-W[i])
    print(2*I[N], W[N]**2 - T)
    return W[N]**2 - T - 2*I[N]  

print("La valeur de la vérification est :", verif())

#travail 3 on fait la trajectoire
mu = 0.5
sigma = 0.5
T = 0.5
N= 100
dt = T/N
def trajectoire(S0, mu, sigma):
    S = [S0]
    for i in range(N):
        S.append(S[i]*np.exp((mu - 0.5*sigma**2)*dt + sigma*mu*np.sqrt(dt)*np.random.normal(0,1)))
    t = np.linspace(0,T,N+1)
    plt.plot(t,S)
    

trajectoire(10, mu, sigma)

#travail 4 on fait 1000 trajectoires
def trajectoires(S0, mu, sigma):
    Nmc = 1000
    for j in range(Nmc):
        trajectoire(S0, mu, sigma)
    plt.title("1000 trajectoires de GBM")
    plt.show()

trajectoires(10, mu, sigma)
    