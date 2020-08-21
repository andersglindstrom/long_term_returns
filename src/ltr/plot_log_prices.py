import ltr.lib

import matplotlib.pyplot as plt

def main():
    data = (1+ltr.lib.load_data()).cumprod()
    plt.semilogy(data)
    plt.show()
