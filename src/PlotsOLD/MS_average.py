import numpy as np
import matplotlib.pyplot as plt

tiefe = [1, 2, 3,4, 5, 6, 7]
time_avergage_NegaMax = []
time_avergage_NegaScout = []
time_avergage_NegaScoutTT = []


fen1 = "tttttttt/8/8/8/8/8/TTTTTTTT r"
alogrithmus = "NegaMax"
nodes = [32, 1056, 14584, 169385, 1161981, 11211857, 72396753]
time = [15.2888, 123.8027, 502.721899, 2824.565601, 14665.3978, 136856.071, 901536.126399]
time_avergage_NegaMax.append(np.average(time))

#bars = plt.bar(tiefe, nodes, color='blue')

algorithmus = "NegaScout"
nodes = [32, 1056, 15961, 129560, 1082641, 6282416, 39055163]
time = [18.836699, 163.3825, 905.5642, 2186.9259, 14378.8425, 85130.4548, 521711.846]
time_avergage_NegaScout.append(np.average(time))

#bars = plt.bar(tiefe, nodes, color='green')

algorithmus = "NegaScoutTT"
nodes = [32, 992, 11221, 85082, 540000, 2937816, 14297526]
time = [11.590901, 94.6219, 592.259501, 2162.491599, 8673.484999, 49043.794599, 255375.011001]
time_avergage_NegaScoutTT.append(np.average(time))




# set width of bar
barWidth = 0.25

# set height of bar
bars1 = [15.2888, 123.8027, 502.721899, 2824.565601, 14665.3978, 136856.071, 901536.126399]
bars2 = [18.836699, 163.3825, 905.5642, 2186.9259, 14378.8425, 85130.4548, 521711.846]
bars3 = [11.590901, 94.6219, 592.259501, 2162.491599, 8673.484999, 49043.794599, 255375.011001]



####################################################################################################

fen2 = "5ww1/2w1wwW1/w1w1wWT1/2wt3W/1wWwwW2/2Tw1WW1/T6T r"
algorithmus = "NegaMax"
nodes = [12, 95, 556, 3048, 10704, 27192, 75753]
time = [5.0266, 17.6148, 64.8634, 238.2309, 597.5455, 1455.7983, 1367.6801]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [12, 95, 996, 4250, 17024, 29384, 64340]
time = [0.1636, 2.444499, 18.5686, 69.5503, 270.6403, 488.8754, 1028.559899]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [12, 49, 152, 1846, 5001, 13044, 27344]
time = [0.1645, 3.2146, 15.3236, 50.1892, 148.3339, 361.5374, 625.436999]
time_avergage_NegaScoutTT.append(np.average(time))





####################################################################################################

fen3 = "t4t1t/3ttw2/2wt4/4w3/W1TW1T2/W1TT1WW1/6T1 g"
algorithmus = "NegaMax"
nodes = [27, 742, 6778, 62263, 331636, 4602160, 23700236]
time = [9.608799, 163.0295, 364.943701, 1266.2351, 4455.1143, 52835.548801, 308398.915399]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [27, 742, 7652, 64558, 295748, 4057794, 17473601]
time = [0.376199, 11.949599, 99.8342, 820.2031, 4287.510699, 50696.479801, 256716.265101]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [27, 671, 5052, 36223, 144164, 1455314, 5831928]
time = [0.3813, 9.0223, 82.7668, 600.3346, 2894.5268, 24609.0518, 122649.4292]
time_avergage_NegaScoutTT.append(np.average(time))

# set height of bar
bars1 = [9.608799, 163.0295, 364.943701, 1266.2351, 4455.1143, 52835.548801, 308398.915399]
bars2 = [0.376199, 11.949599, 99.8342, 820.2031, 4287.510699, 50696.479801, 256716.265101]
bars3 = [0.3813, 9.0223, 82.7668, 600.3346, 2894.5268, 24609.0518, 122649.4292]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]


####################################################################################################

fen4 = "8/1t6/1Ww1w3/1TWw4/8/1T1w4/8 g"
algorithmus = "NegaMax"
nodes = [3, 6, 21, 30, 30, 30, 30]
time = [7.1956, 1.643099, 4.433499, 5.000001, 4.6766, 5.864601, 10.9367]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [3, 6, 23, 30, 30, 30, 30]
time = [0.0332, 0.0867, 0.240401, 0.3994, 0.506399, 0.749399, 1.017399]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [3, 5, 19, 30, 30, 30, 30]
time = [0.082199, 0.0912, 0.2519, 0.382801, 0.5161, 0.7008, 0.811]
time_avergage_NegaScoutTT.append(np.average(time))


# set height of bar
bars1 = [7.1956, 1.643099, 4.433499, 5.000001, 4.6766, 5.864601, 10.9367]
bars2 = [0.0332, 0.0867, 0.240401, 0.3994, 0.506399, 0.749399, 1.017399]
bars3 = [0.082199, 0.0912, 0.2519, 0.382801, 0.5161, 0.7008, 0.811]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]



####################################################################################################

fen5 = "3t4/4wwww/2tt4/3cC3/4TT2/WWWW4/2T5 r"
algorithmus = "NegaMax"
nodes = [22, 22, 22, 22, 22, 22, 22]
time = [8.825301, 6.963201, 6.548199, 3.7062, 4.3921, 3.2194, 5.1109]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [22, 22, 22, 22, 22, 22, 22]
time = [0.2906, 0.2421, 0.2216, 0.2203, 0.2625, 0.2309, 0.217099]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [22, 22, 22, 22, 22, 22, 22]
time = [0.274499, 0.2811, 0.2477, 0.2434, 0.2449, 0.2428, 0.242]
time_avergage_NegaScoutTT.append(np.average(time))



# set height of bar
bars1 = [8.825301, 6.963201, 6.548199, 3.7062, 4.3921, 3.2194, 5.1109]
bars2 = [0.2906, 0.2421, 0.2216, 0.2203, 0.2625, 0.2309, 0.217099]
bars3 = [0.274499, 0.2811, 0.2477, 0.2434, 0.2449, 0.2428, 0.242]



####################################################################################################

fen6 = "5ww1/2w1wwW1/w1w1wWT1/2wt3W/1wWwwW2/2Tw1WW1/T6T r"
algorithmus = "NegaMax"
nodes = [12, 95, 556, 3048, 10704, 27192, 75753]
time = [4.3952, 13.7041, 50.393, 207.6194, 460.2962, 1259.918, 1316.2962]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [12, 95, 996, 4250, 17024, 29384, 64340]
time = [0.132399, 1.512199, 12.011899, 52.0283, 206.6284, 483.8984, 1072.6467]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [12, 49, 152, 1846, 5001, 13044, 27344]
time = [0.1994, 1.239, 10.9549, 38.9226, 114.747099, 270.787299, 624.175499]
time_avergage_NegaScoutTT.append(np.average(time))


####################################################################################################


fen7 = "tt6/6w1/twtt1tW1/3w1WT1/W1TTWW2/1TW1W3/8 r"
algorithmus = "NegaMax"
nodes = [17, 482, 2158, 30227, 146240, 1339749, 7378158]
time = [6.630301, 49.5123, 173.586901, 1514.873999, 2503.352401, 16955.3573, 99542.112501]
time_avergage_NegaMax.append(np.average(time))

algorithmus = "NegaScout"
nodes = [17, 482, 2613, 31755, 147782, 998036, 4950329]
time = [0.239999, 6.710599, 37.0048, 405.384901, 2117.289099, 14009.742, 69708.0623]
time_avergage_NegaScout.append(np.average(time))

algorithmus = "NegaScoutTT"
nodes = [17, 426, 1665, 19107, 80256, 489821, 2150201]
time = [0.2293, 5.962, 32.5155, 387.3726, 1499.0953, 8720.589701, 38242.7805]
time_avergage_NegaScoutTT.append(np.average(time))




####################################################################################################

fen8 = "2wwwww1/2twttt1/1w1TT3/W1WWWTw1/4T3/8/3T3T r"
algorithmus = "NegaMax"
nodes = [33, 390, 5579, 36998, 160093, 160093, 160093]
time = [12.8495, 73.6168, 361.629999, 1442.9229, 2122.1625, 2028.1006, 2046.4587]
time_avergage_NegaMax.append(np.average(time))


algorithmus = "NegaScout"
nodes = [33, 390, 6633, 31474, 136746, 136746, 136746]
time = [0.367, 6.4516, 74.5561, 464.2147, 1854.5062, 2007.037501, 1994.400401]
time_avergage_NegaScout.append(np.average(time))


algorithmus = "NegaScoutTT"
nodes = [33, 316, 4323, 17725, 83267, 83267, 83267]
time = [0.511799, 6.3292, 67.800101, 384.0589, 1543.0196, 1553.6229, 1552.5512]
time_avergage_NegaScoutTT.append(np.average(time))




####################################################################################################


print("NegaMax: " + str(np.average(time_avergage_NegaMax)))
print("NegaScout " + str(np.average(time_avergage_NegaScout)))
print("NegaScoutTT: " + str(np.average(time_avergage_NegaScoutTT)))