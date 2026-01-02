# binomial-option-pricer-
A clean, efficient Python implementation of the binomial tree model for pricing European and American call/put options. This project demonstrates lattice-based numerical methods for option valuation, handling early exercise features in American options through dynamic programming on a recombining tree.

#Key Features
Supports both European and American styles for calls and puts.
Adjustable parameters: underlying price,strike,time to maturity, risk-free rate, volatility, and number of steps.
Efficient computation with vectorized operations( using NumPy for performance )
Optional dividend yield support for more realistic modeling
Visualizations of the binomial tree and payoff diagrams ( via Matplotlip )

#Motivation
Option pricing is a cornerstone for quantitative finance. The binomial model provides an intuitive, discrete-time approximation to the Black-Scholes framework, making it ideal for educational purposes and scenarios with path-dependent features like early exercise. 

