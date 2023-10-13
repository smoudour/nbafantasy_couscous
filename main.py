# Things to test
from .api_data import *
from .box_score_functions import compare_season, matchup_outcome, against_all, get_teams_stats
# from espn_api.basketball import League


# Get number of total matchups - duration of league
# does it get the total or the current matchup period? remains to be seen...
league_dur = my_league._fetch_league()['status']['currentMatchupPeriod']

# Get results for projected matchups between FaCT and Guatemala Parrots
faliro_season_vs_strogg = compare_season('Faliro City Tricksters ', 'Brooklyn  Strogguloi', my_league, season_length=league_dur)

# Get results for projected matchups between FaCT and all other teams for Week X
week = 1
my_team = 'Faliro City Tricksters '
week_boxscore = my_league.box_scores(matchup_period=week)
week_boxscore_stats = get_teams_stats(week_boxscore)
faliro_vs_all_week = against_all(my_team, week_boxscore_stats)

for week in faliro_season_vs_strogg.keys():
    print(f'{week}: {matchup_outcome(faliro_season_vs_strogg[week])}')


for team in faliro_vs_all_week.keys():
    print(f'{team}: {matchup_outcome(faliro_vs_all_week[team])}')

