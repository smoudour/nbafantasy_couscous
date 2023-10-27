import matplotlib.pyplot as plt
from matplotlib import colors
from box_score_functions import *
from pandas import DataFrame

def color_outcomes(outcome: str) -> int:
    if outcome == 'W':
        return 0
    elif outcome == 'L':
        return 1
    elif outcome == 'D':
        return 2



# this doesnt make sense to be presented as a plot... Better be a table with the structure of
# heatmap like, with little squares representing each opponent team / or other week, coloured 
# depending on the outcome (green-win, red-lose, orange-draw) and inside a number stating the number
# of category wins for team being compared.
def plotSeasonComparison(team1: str, team2: str, wins_comp: DataFrame, outcomes_comp: DataFrame):
    # Plots single graph of total category wins per matchup VS one specific team for the whole Season
    x = list(wins_comp['Var'])
    wins_n = list(wins_comp['Wins'])
    # Fix mask for cases of W-L or W-L-D results to contain respectively 2 or 3 colors.
    mask = list(map(color_outcomes, outcomes_comp['Outcome']))

    fig, ax = plt.subplots()
    cmap =  colors.ListedColormap(['green', 'red', 'orange'])

    scatter = ax.scatter(x, wins_n, c=mask, cmap=cmap)
    ax.plot(x, wins_n, c='k', linewidth=0.4, alpha=0.7)
    # ax.axhline(x, y=5, color='green')
    # ax.fill_between(x,0,4.5, color='red', alpha=0.2)
    # ax.fill_between(x,4.5,9,color='green', alpha=0.2)
    ax.set_ylabel('Category Wins')
    ax.tick_params(axis='x', which='major', labelsize=6)
    ax.set_title(f'{team1} VS {team2}')
    # produce a legend with the unique colors from the scatter
    handles = scatter.legend_elements()
    ax.legend(title="Matchup", handles=handles[0], labels=['Win', 'Lose', 'Draw'])
    plt.show()
