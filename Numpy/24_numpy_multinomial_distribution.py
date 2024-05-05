# Multinomial dist: it is a generalizaiton of binomial distribution

# parameter - n(number of possibilities or outcome {no of dice roll}), pvals(list of possibilities {no of possible outcome}), size(shape of returned array)
from numpy import random
x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)


# multinomial samples will not produce a single value, they will produce one value for each pvals (ist of possibilities)
