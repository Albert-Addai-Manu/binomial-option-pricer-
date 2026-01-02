import numpy as np

def binomial_price(S0, K, T, r, sigma, N, option_type="call", american=False):
    """
    Cox-Ross-Rubinstein Binomial Model
    
    Parameters:
    - S0: initial stock price
    - K: strike
    - T: time to maturity (years)
    - r: risk-free rate
    - sigma: volatility
    - N: number of time steps
    - option_type: "call" or "put"
    - american: True for American, False for European
    
    Returns: option price
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))      # up factor
    d = 1 / u                            # down factor (recombining)
    p = (np.exp(r * dt) - d) / (u - d)   # risk-neutral probability
    
    # Stock price tree (we only need the final layer for European, but full for American)
    stock = np.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(i+1):
            stock[j, i] = S0 * (u ** (i - j)) * (d ** j)
    
    # Option value at maturity
    if option_type == "call":
        option = np.maximum(stock[:, N] - K, 0)
    else:  # put
        option = np.maximum(K - stock[:, N], 0)
    
    # Backward induction
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            eu_value = np.exp(-r * dt) * (p * option[j] + (1 - p) * option[j+1])
            if american:
                # Early exercise for American
                if option_type == "call":
                    exercise = stock[j, i] - K
                else:
                    exercise = K - stock[j, i]
                option[j] = max(eu_value, exercise)
            else:
                option[j] = eu_value
    
    return option[0]


def binomial_option_price():
    return None