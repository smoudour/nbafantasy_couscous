from .api_data import *
from espn_api.basketball import League, Team
from espn_api.basketball.box_score import BoxScore
import pandas as pd

# logic
# week_bs = my_league.box_scores(matchup_period=1)

#Compares box score of team 1 over team 2 and presents a result if these two teams were fighting together in this week
def compare_per_week(team1, team2, week_boxscore: BoxScore) -> pd.DataFrame:

    team1_flag = True
    team2_flag = True
    index = 0

    while team1_flag or team2_flag:
    # for box_score in week_boxscore:
        if team1 == week_boxscore[index].home_team.team_name:
            team1_stats = week_boxscore[index].home_stats
            team1_flag = False
        if team1 == week_boxscore[index].away_team.team_name:
            team1_stats = week_boxscore[index].away_stats
            team1_flag = False
        if team2 == week_boxscore[index].home_team.team_name:
            team2_stats = week_boxscore[index].home_stats
            team2_flag = False
        if team2 == week_boxscore[index].away_team.team_name:
            team2_stats = week_boxscore[index].away_stats
            team2_flag = False
        index += 1

    team1_stat_values = [value['value'] for value in team1_stats.values()]
    team2_stat_values = [value['value'] for value in team2_stats.values()]
    cat = list(team1_stats.keys())
    result = []

    zip_object = zip(team1_stat_values, team2_stat_values)
    for value1, value2 in zip_object:
        if value1 > value2:
            result.append('W')
        elif value1 < value2:
            result.append('L')
        else:
            result.append('D')
    

    d = {'Cat' : cat, team1 : team1_stat_values, team2 : team2_stat_values, 'Result' : result}
    result_df = pd.DataFrame(data=d)

    return result_df



def compare_season(team1: str, team2: str, league: League, season_length: int) -> dict:

    result_df = {}
    for week in range(1,season_length+1):
        week_boxscore = league.box_scores(matchup_period=week)
        df = compare_per_week(team1, team2, week_boxscore)
        result_df[f'Week {week}'] = df

    return result_df


def fix_categories(box_scores: pd.DataFrame, included_cat: list = categories) -> pd.DataFrame:

    fixed_results = {}
    for week in box_scores.keys():
        try:
            box_scores[week].set_index(keys='Cat', inplace=True)
        except:
            print('Already indexed!')

        df = box_scores[week].loc[included_cat]
        fixed_results[week] = df

    return fixed_results


def wins_per_week(season_comparison: dict) -> pd.DataFrame:

    weeks = list(season_comparison.keys())
    wins_list = []

    for week in weeks:
        wins = sum(season_comparison[week]['Result'] == 'W')
        wins_list.append(wins)
    
    d = {'Week' : weeks, 'Wins' : wins_list}
    result = pd.DataFrame(data = d)

    return result



# TO IMPLEMENT 

# 1.How would a fantasy team perform compared to all other teams that week.
# From the head-to-head table, we estimate the percentage of matchups that a team would have won against all other teams in the league, and its average score. 
# If a fantasy team lost a matchup but would have won 90% of all other matchups, it means that the team is still strong, but was unlucky as it played with the strongest opponent in the league. 
# Do not change much. 
# On the hand if a team won the matchup but would have won only 20% of the matchups, it implies that the team got lucky and played with the weakest opponent in the league, so changes should be made. 
# The percentage of wins across the league, puts the win/loss into perspective.

def fix_team_stats(team_stats: dict, categories: list) -> dict:

    fixed_team_stats = {key: team_stats[key] for key in categories}
    return fixed_team_stats
    

# Get team stats for every team for a specific week
def get_teams_stats(week_boxscores: list) -> dict:

    teams_stats = {}
    for boxscore in week_boxscores:
        team_name_1 = boxscore.home_team.team_name
        team_stats_1 = boxscore.home_stats
        team_name_2 = boxscore.away_team.team_name
        team_stats_2 = boxscore.away_stats
        teams_stats[team_name_1] = fix_team_stats(team_stats_1, categories=categories)
        teams_stats[team_name_2] = fix_team_stats(team_stats_2, categories=categories)


    return teams_stats

# Compare stats of a specifed team against all others for given week
def against_all(my_team: str, week_matchups: dict) -> pd.DataFrame:
    my_team_stats = [value['value'] for value in week_matchups[my_team].values()]
    categories = list(week_matchups[my_team].keys())
    totals = {}

    for team in week_matchups.keys():
        if my_team != team:
            op_team_stats = [value['value'] for value in week_matchups[team].values()]
            result = []
            zip_object = zip(my_team_stats, op_team_stats)
            for value1, value2 in zip_object:
                if value1 > value2:
                    result.append('W')
                elif value1 < value2:
                    result.append('L')
                else:
                    result.append('D')

            d = {'Cat' : categories, my_team : my_team_stats, team : op_team_stats, 'Result' : result}
            result_df = pd.DataFrame(data=d)
            totals[team] = result_df

    return totals  
