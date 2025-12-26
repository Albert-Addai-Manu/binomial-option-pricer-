from binomial import test_binomial
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes for comparison
def black_scholes(S0, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == "call":
        return S0 * norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    else:
        return K*np.exp(-r*T)*norm.cdf(-d2) - S0*norm.cdf(-d1)

# Parameters
S0 = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2

# Test European call
print("European Call:")
bs_call = black_scholes(S0, K, T, r, sigma, "call")
print(f"Black-Scholes: {bs_call:.4f}")

for N in [10, 50, 100, 200]:
    binom = binomial_price(S0, K, T, r, sigma, N, "call", american=False)
    print(f"N={N:3d}: {binom:.4f} (diff: {abs(binom - bs_call):.5f})")

# American put (Black-Scholes doesn't price American!)
print("\nAmerican Put:")
bs_put = black_scholes(S0, K, T, r, sigma, "put")
print(f"European Put (BS): {bs_put:.4f}")
american_put = binomial_price(S0, K, T, r, sigma, N=200, option_type="put", american=True)
print(f"American Put (N=200): {american_put:.4f} (early exercise premium: {american_put - bs_put:.4f})")

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes function ...
# Parameters ...
# Tests and print statements ...
