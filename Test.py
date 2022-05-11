import pandas as pd
import netCDF4 as nc
from matplotlib import pyplot as plt
import progressbar
import numpy as np
from geopy.distance import geodesic
from itertools import product
from time import time
from progressbar import progressbar
from scipy.signal import lombscargle
import math
import matplotlib.pyplot as plt


def f(value):
    return math.sin(2*value)


x = range(100)
y = [f(i) for i in x]
w = np.linspace(0.01, math.pi + 0.2, 100)

result = lombscargle(x, y, w)

plt.plot(w, result)
plt.show()



