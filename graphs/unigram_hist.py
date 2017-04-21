import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

N = 10
x = np.arange(N)

# entertainment
y = (3085, 2165, 1603, 1436, 1427, 1371, 1302, 1260, 1165, 1043)
plt.subplot(2, 4, 1)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('new', 'video', '#oscars', 'says', 'star', 'watch',
                'best', 'trump', 'first', 'see'))
plt.title('Entertainment')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# games
y = (3083, 2007, 1926, 1696, 1679, 1546, 1492, 1455, 1342, 1339)
plt.subplot(2, 4, 2)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('new', 'available', 'game', '2', 'steam', 'games',
                'get', '#steam...', 'ps4', 'one'))
plt.title('Games')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# weather
y = (4539, 3824, 3636, 2888, 2851, 2709, 2704, 2668, 2398, 2389)
plt.subplot(2, 4, 3)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('rain', 'warning', 'tornado', 'pm', 'weather', 'snow',
                'day', 'cst', 'forecast', 'today'))
plt.title('Weather')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# science
y = (3761, 2390, 1982, 1862, 1669, 1367, 1277, 1255, 1157, 1047)
plt.subplot(2, 4, 4)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('new', 'science', 'scientists', 'via', 'could', 'may',
                'us', 'space', 'first', 'one'))
plt.title('Science')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# sports
y = (1892, 1418, 1201, 1171, 1129, 1105, 1097, 1081, 1076, 1070)
plt.subplot(2, 4, 5)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('game', 'win', 'new', 'team', 'vs', 'via', 'nfl',
                'one', 'first', 'season'))
plt.title('Sports')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# politics
y = (9123, 3440, 2789, 2277, 2122, 2092, 1993, 1975, 1680, 1616)
plt.subplot(2, 4, 6)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('trump', 'says', 'trump\'s', 'brexit', 'president',
                'new', 'donald', 'house', '#hw', 'may'))
plt.title('Politics')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# technology
y = (2941, 2448, 1827, 1722, 1625, 1450, 1266, 1126, 908, 849)
plt.subplot(2, 4, 7)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('technology', 'new', '#cdntech', 'data', 'google',
                'apple', 'tech', 'facebook', 'app', 'says', 'big'))
plt.title('Technology')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# fun
y = (2683, 2225, 2120, 1905, 1905, 1749, 1603, 1567, 1315, 1224)
plt.subplot(2, 4, 8)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('like', 'i\'m', 'it\'s', 'people', 'green', 'don\'t',
                'get', 'one', 'blue', 'u'))
plt.title('Fun')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

plt.tight_layout()

fig = plt.gcf()
fig.set_size_inches(10, 5)

plt.savefig('unigram_hist.png', format='png', dpi=1000)
