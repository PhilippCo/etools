import numpy as np

# E-Reihen
E3  = [1, 2.2, 4.7]

E6  = [1.0, 1.5, 2.2, 3.3, 4.7, 6.8]

E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3,
       3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

E48 = [1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.33, 1.4, 1.47, 1.54, 1.62,
        1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74,
        2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64,
        4.87, 5.11, 5.36, 5.62, 5.9, 6.19, 6.49, 6.81, 7.15, 7.5, 7.87,
        8.25, 8.66, 9.09, 9.53]

E96 = [1.0, 1.02, 1.05, 1.07, 1.1, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27,
        1.3, 1.33, 1.37, 1.4, 1.43, 1.47, 1.5, 1.54, 1.58, 1.62, 1.65,
        1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2, 2.05, 2.1, 2.15,
        2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.8,
        2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.4, 3.48, 3.57, 3.65,
        3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75,
        4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.9, 6.04, 6.19,
        6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.5, 7.68, 7.87, 8.06,
        8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]


# Funktion um den nächsten Wert aus der übergebenen E-Reihe zu finden
def find_in_E(array,value):
    array = np.array(array) * 10**(np.ceil(np.log10(value))-1)
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def find_ratio(eseries, ratio):
    all = np.array([])
    for pow in range(0, 7):
        all = np.concatenate([all, np.array(eseries)*10**pow])

    ratios = []
    for res in all:
        for res2 in all:
            ratios.append(res/res2)

    ratios = np.array(ratios)
    ratios = abs(ratios - ratio)

    mini = np.where( ratios == np.min(ratios) )[0][0]
    return all[int(mini/len(all))], all[mini%len(all)]


def find_voltdiv(eseries, uin, uout):
    return find_ratio(eseries, uin/uout-1)



if __name__ == "__main__":
    #findet aus E23 den Wert, der am nächsten an 3 ist
    #print( find_ratio(E24, 3) )


    print( find_voltdiv(E24, 13.4, 2) )
