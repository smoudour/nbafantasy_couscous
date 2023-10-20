import matplotlib.pyplot as plt
from matplotlib import colors
from box_score_functions import *

results = compare_season('Faliro City Tricksters ', 'Guatemala Parrots', my_league, league_duration)
wins = wins_per_matchup(results)



# Plots single graph of total category wins per matchup VS one specific team for the whole Season

teams = list(wins['Week'])
outcomes = list(wins['Wins'])
mask = list(wins['Wins']>4)

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
