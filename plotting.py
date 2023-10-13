import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors
from box_score_functions import *

results = compare_season('Faliro City Tricksters ', 'Guatemala Parrots', my_league, 20)
results = fix_categories(results)
wins = wins_per_week(results)


# To create matrix of dimensions [ len(wins_list)/X, X ]
# m = []
# X = 4
# wins_list = list(wins['Wins'])

# while wins_list != []:
#     m.append(wins_list[:X])
#     wins_list = wins_list[X:]

teams = list(wins['Week'])
outcomes = list(wins['Wins'])
mask = list(wins['Wins']>4)



# plots single graph of total category wins per matchup VS one specific team
team1 = 'Faliro City Tricksters '
team2 = 'Guatemala Parrots'

fig, ax = plt.subplots()
cmap =  colors.ListedColormap(['red', 'green'])

scatter = ax.scatter(teams, outcomes, c=mask, cmap=cmap)
ax.plot(teams, outcomes, c='k', linewidth=0.4, alpha=0.7)
ax.axhline(teams, y=5, color='green')
ax.fill_between(teams,0,4.5, color='red', alpha=0.2)
ax.fill_between(teams,4.5,9,color='green', alpha=0.2)
ax.set_ylabel('Category Wins')
ax.tick_params(axis='x', which='major', labelsize=6)
ax.set_title('VS Guatemala Parrots')
# produce a legend with the unique colors from the scatter
handles = scatter.legend_elements()
ax.legend(title="Matchup", handles=handles[0], labels=['Lost', 'Won'])
plt.show()
