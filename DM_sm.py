import numpy as np

# Paramètres de simulation
T = 1       
N = 1000       
Nmte = 10000      
dt = T / N
t = np.linspace(0, T, N+1)

# Simuler les trajectoires browniennes
dW = np.sqrt(dt) * np.random.randn(Nmte, N)
W = np.cumsum(dW, axis=1)
W = np.concatenate((np.zeros((Nmte,1)), W), axis=1)  # W_0 = 0

# Fonction et ses dérivées
def f(t, x): 
    return t * np.sin(x)
def f_t(x): 
    return np.sin(x)
def f_x(t, x): 
    return t * np.cos(x)
def f_xx(t, x): 
    return -t * np.sin(x)

# Partie gauche : f(T, W_T) - f(0, W_0)
lhs = f(T, W[:, -1]) - f(0, W[:, 0])

# Partie droite :
rhs = np.zeros(Nmte)
for i in range(N):
    rhs += f_t(W[:, i]) * dt + f_x(t[i], W[:, i]) * dW[:, i] + 0.5 * f_xx(t[i], W[:, i]) * dt

# Comparaison
error = lhs - rhs

print("Moyenne de l’erreur :", np.mean(error))
print("Écart-type de l’erreur :", np.std(error))
print("valeurs :", np.mean(lhs))
