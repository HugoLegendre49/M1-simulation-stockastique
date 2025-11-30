import numpy as np
import matplotlib.pyplot as plt

#parametres
r=0.1
delta=0.5
T=0.5
K=10
Nme=10000

def St(S0):
    return S0*np.exp((r-(delta**2)/2)*T + delta*np.sqrt(T)*np.random.normal(0,1))

# return le prix d'un call
def Prix_Call(S0):
    debug = False
    gain=[]
    for i in range(Nme):
        gain.append(np.maximum(0,St(S0)-K))
        if debug:
            print(f"Simulation {i+1}: Prix final de l'actif = {St(S0)[i]:.2f}, Gain = {gain[-1]:.2f}")

    return np.exp(-r*T)*np.mean(gain)

#fonction du graphique de cell normal
def graphe_cell():
    S0 = np.arange(0, 20, 0.5)
    prix = np.array([Prix_Call(s) for s in S0])
    payoff = np.maximum(0, S0-K)

    plt.plot(S0, payoff, label='Payoff du Call', color='red')
    plt.plot(S0, prix, label='Prix du Call', color='blue')
    plt.xlabel('Prix initial de l\'actif sous-jacent S0')
    plt.show()

# fonction de buterfly
def pay_off(S0):
    gain=[]
    for i in range(Nme):
        pay_off = np.maximum(0, St(S0)-K)+np.maximum(0, St(S0)- 3*K)-np.maximum(0, St(S0)-2*K)*2
        gain.append(pay_off)
    prix = np.exp(-r*T)*np.mean(gain)
    return prix

def graphe_buterfly():
    S0 = np.arange(0, 40, 0.5)
    prix = np.array([pay_off(s) for s in S0])
    payoff = np.maximum(0, S0-K)+np.maximum(0, S0- 3*K)-np.maximum(0, S0-2*K)*2

    plt.plot(S0, payoff, label='Payoff du Buterfly', color='red')
    plt.plot(S0, prix, label='Prix du Buterfly', color='blue')
    plt.xlabel('Prix initial de l\'actif sous-jacent S0')
    plt.show()



# Affichage du graphe
graphe_cell()
graphe_buterfly()
print("Prix du Call pour S0=10:", Prix_Call(10))






