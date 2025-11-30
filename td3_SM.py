#td3_SM
import matplotlib as np

# parametre : 
r = 0.07
T = 1
mu = 0.12
sigma1 = 0.3
sigma2 = 0.4
p = 2
lambda1 = 0.005
X0 = 100
M0= 500
P0 = 100
N= 100
Nmc = 10000
dT=T/N

# fonction d'utiliter

def U(x):
    return np.log(x)

# procesus stochastique Mt, Pt, Xt

Mt = np.zeros(N+1)
Pt = np.zeros(N+1)
Xt = np.zeros(N+1)
Mt[0] = M0
Pt[0] = P0
Xt[0] = X0
for i in range(1,N+1):
    g = random.normal(0,1)
    Mt[i]= Mt[i-1]-g*Mt[i-1]*dT + lambda2*np.sqrt(dt)
    
