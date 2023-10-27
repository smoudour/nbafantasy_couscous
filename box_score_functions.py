from api_data import *
from espn_api.basketball.box_score import H2HCategoryBoxScore
from espn_api.basketball import League
import pandas as pd

# Get only categories of interest, reference in 'categories' list
# def fix_team_stats(team_stats: dict, categ: list = categories) -> dict:

#     fixed_team_stats = {key: team_stats[key] for key in categ}
#     return fixed_team_stats
    

# Get team stats for every team for a specific week
# Take Boxscore Class from .box_scores method of Leage Class and transform it to a dict, containing only categories we care about. 
def boxscores_to_dict(week_boxscores: list[H2HCategoryBoxScore]) -> dict:

    teams_stats = {}
    for boxscore in week_boxscores:
        team_name_1 = boxscore.home_team.team_name
        team_name_2 = boxscore.away_team.team_name
        teams_stats[team_name_1] = boxscore.home_stats
        teams_stats[team_name_2] = boxscore.away_stats

    return teams_stats


# Function to compare desired categories (passed through categories argv) between two teams and produce outcome per category (W, L or D)
# team stats are passed in a boxscore dictionary format, transformed with boxscores_to_dict function
def compare_cats(team_1_stats: dict, team_2_stats:dict, categories: list[str] = categories) -> list:

    result = []
    team1_stats_values = []
    team2_stats_values = []

    # decide projected matchup outcome
    for category in categories:
        team1_value = team_1_stats[category]['value']
        team2_value = team_2_stats[category]['value']
        team1_stats_values.append(team1_value)
        team2_stats_values.append(team2_value)

        if category == 'TO':
            if team1_value > team2_value:
                result.append('L')
            elif team1_value < team2_value:
                result.append('W')
            else:
                result.append('D')
        else:
            if team1_value > team2_value:
                result.append('W')
            elif team1_value < team2_value:
                result.append('L')
            else:
                result.append('D')

    return [team1_stats_values, team2_stats_values, result]

# Compares box score of team 1 VS team 2 for specified week
def compare_week(team1: str, team2: str, week_boxscore: dict, categories:list = categories) -> pd.DataFrame:

    # Find desired teams: team1 & team2
    teams = list(week_boxscore.keys())
    team1_flag = False
    team2_flag = False
    for team in teams:
        if team1 == team:
            team1_stats = week_boxscore[team]
            team1_flag = True
        elif team2 == team:
            team2_stats = week_boxscore[team]
            team2_flag = True
        if team1_flag and team2_flag:
            break

    # Create dataframe with results VS designated team
    results = compare_cats(team1_stats, team2_stats)
    d = {'Cat' : categories, team1 : results[0], team2 : results[1], 'Result' : results[2]}
    matchup = pd.DataFrame(data=d)

    return matchup

# Compares projected results of team 1 VS team 2 for the whole season
def compare_season(team1: str, team2: str, league: League, season_length: int) -> dict[pd.DataFrame]:

    matchups = {}
    for week in range(1,season_length+1):
        boxscores = league.box_scores(matchup_period=week)
        bxsc_dict = boxscores_to_dict(boxscores)
        matchup = compare_week(team1, team2, bxsc_dict)
        matchups[f'Week {week}'] = matchup

    return matchups

# How would a fantasy team perform compared to all other teams that week.
# From the head-to-head table, we estimate the percentage of matchups that a team would have won against all other teams in the league, and its average score. 
# If a fantasy team lost a matchup but would have won 90% of all other matchups, it means that the team is still strong, but was unlucky as it played with the strongest opponent in the league. 
# Do not change much. 
# On the hand if a team won the matchup but would have won only 20% of the matchups, it implies that the team got lucky and played with the weakest opponent in the league, so changes should be made. 
# The percentage of wins across the league, puts the win/loss into perspective.

# Compare stats of a specifed team against all others for given week
def against_all_week(my_team: str, week_matchups: dict, categories: list = categories) -> pd.DataFrame:

    my_team_stats = week_matchups[my_team]
    totals = {}

    for opp_team in week_matchups.keys():
        if my_team != opp_team:
            opp_team_stats = week_matchups[opp_team]

            result = compare_cats(my_team_stats, opp_team_stats)
            d = {'Cat' : categories, my_team : result[0], opp_team : result[1], 'Result' : result[2]}
            result_df = pd.DataFrame(data=d)

            totals[opp_team] = result_df

    return totals  


# Calculate wins of team 1 VS team 2 for each matchup
# Doesn't decide the matchup outcome, just counts the number of wins.
def wins_per_matchup(matchups: dict) -> pd.DataFrame:

    keys = list(matchups.keys())
    wins_list = []

    for key in keys:
        wins = sum(matchups[key]['Result'] == 'W')
        wins_list.append(wins)
    
    d = {'Var' : keys, 'Wins' : wins_list}
    df = pd.DataFrame(data = d)

    return df

# Calculate outcome for projected matchups
def matchup_outcome(single_matchup: pd.DataFrame) -> str:

    wins = sum(single_matchup['Result'] == 'W')
    loses = sum(single_matchup['Result'] == 'L')

    if wins == loses:
        return 'D'
    elif wins > loses:
        return 'W'
    else:
        return 'L'
    
def matchups_outcome(all_matchups: dict[pd.DataFrame]) -> pd.DataFrame:

    outcomes = []
    for key in all_matchups.keys():
        matchup = all_matchups[key]
        outcomes.append(matchup_outcome(matchup))

    d = {'Var' : all_matchups.keys(), 'Outcome' : outcomes}
    df = pd.DataFrame(data=d)
    return df