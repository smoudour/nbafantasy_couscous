# Things to test
from api_data import *
from box_score_functions import *
# from espn_api.basketball import League

team1 = 'Faliro City Tricksters '
team2 = 'Guatemala Parrots'

# General workflow for comparisons
# get league
my_league = League(league_id=credentials['leagueID '], year=credentials['year'], espn_s2=credentials['espn_s2'], swid=credentials['swid'])
# get league duration
# does it get the total or the current matchup period? remains to be seen...
league_dur = my_league._fetch_league()['status']['currentMatchupPeriod']
# get boxscores
week_boxscores = my_league.box_scores(1)
boxscores_dict = boxscores_to_dict(week_boxscores)


# BASIC DATA STRUCTURE WHERE ALL ANALYSIS BASED - COMPARISON DICT
# Calculate comparison for whole season between team 1 and team 2
season_comp = compare_season(team1, team2, my_league, league_dur)
# Calculate comparison for selected week between team 1 and everyone
week_vs_all = against_all_week(team1, boxscores_dict)

# Calculate outcome for every matchup in the above comparisons
outcome_season_comp = matchups_outcome(season_comp)
outcome_week_vs_all = matchups_outcome(week_vs_all)

# Calculate No of wins for every matchup in the above comparisons
wins_season_comp = wins_per_matchup(season_comp)
wins_week_vs_all = wins_per_matchup(week_vs_all)
