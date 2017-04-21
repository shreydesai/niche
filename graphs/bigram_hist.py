import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

N = 10
x = np.arange(N)

# entertainment
y = (398, 326, 297, 267, 210, 178, 175, 156, 156, 152)
plt.subplot(2, 4, 1)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(red, carpet)', '(donald, trump)', '(box, office)',
                '(best, picture)', '(super, bowl)', '(star, wars)',
                '(la, la)', '(wins, best)', '(kim, kardashian)',
                '(via, @toofab)'))
plt.title('Entertainment')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# games
y = (767, 710, 451, 418, 375, 288, 282, 269, 232, 224)
plt.subplot(2, 4, 2)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(daily, deal)', '(resident, evil)', '(nintendo, switch)',
                '(mass, effect)', '(xbox, one)', '(effect, andromeda)',
                '(final, fantasy)', '(star, wars)', '(@steam..., daily)',
                '(@mine..., #stor...)'))
plt.title('Games')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# weather
y = (3108, 1164, 1060, 974, 952, 793, 740, 729, 726, 687)
plt.subplot(2, 4, 3)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(tornado, warning)', '(cst, #spc)', '(cdt, tornado)',
                '(pm, cdt)', '(cst, tornado)', '(#atxwx, #atxweather)',
                '(heavy, rain)', '(#spc, day1)', '(pm, cst)',
                '(thunderstorm, outlook)'))
plt.title('Weather')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# science
y = (521, 241, 208, 197, 182, 167, 145, 143, 142, 138)
plt.subplot(2, 4, 4)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(climate, change)', '(years, ago)', '(study, finds)',
                '(new, study)', '(new, video)', '(new, species)',
                '(black, hole)', '(solar, system)', '(first, time)',
                '(could, help)'))
plt.title('Science')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# sports
y = (602, 347, 257, 241, 240, 225, 198, 189, 168, 166)
plt.subplot(2, 4, 5)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(super, bowl)', '(tom, brady)', '(lebron, james)',
                '(russell, westbrook)', '(ncaa, tournament)',
                '(years, ago)', '(kevin, durant)', '(last, night)',
                '(steph, curry)', '(demarcus, cousins)'))
plt.title('Sports')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# politics
y = (1474, 1120, 1048, 894, 646, 629, 549, 543, 537, 429)
plt.subplot(2, 4, 6)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(donald, trump)', '(white, house)', '(#hw, #cdnpoli)',
                '(theresa, may)', '(president, trump)', '(supreme, court)',
                '(health, care)', '(travel, ban)', '(jeremy, corbyn)',
                '(donald, trump\'s)'))
plt.title('Politics')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# technology
y = (390, 329, 294, 290, 228, 189, 187, 186, 167, 158)
plt.subplot(2, 4, 7)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(big, data)', '(machine, learning)', '(via, @verge)',
                '(artificial, intelligence)', '(data, science)',
                '(silicon, valley)', '(fake, news)', '(windows, 10)',
                '(virtual, reality)', '(social, media)'))
plt.title('Technology')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

# fun
y = (180, 165, 164, 154, 141, 137, 124, 117, 115, 97)
plt.subplot(2, 4, 8)
plt.bar(x, y, color='#003249')
plt.xticks(x, ('(donald, trump)', '(eve, eve)', '(looks, like)',
                '(harry, potter)', '(don\'t, know)', '(happy, birthday)',
                '(i\'m, going)', '(every, time)', '(look, like)',
                '(last, night)'))
plt.title('Fun')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

plt.tight_layout()

fig = plt.gcf()
fig.set_size_inches(10, 5)

plt.savefig('bigram_hist.png', format='png', dpi=1000)
