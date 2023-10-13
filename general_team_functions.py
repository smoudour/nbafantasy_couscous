from espn_api.basketball import League
from espn_api.basketball import Team

# Find correct name of team from League object 
def getTeam(league: League, teamname:str = None) -> Team:
    for team in league.teams:
        if teamname in team.team_name:
            print(team.team_name)
            return team

# Get **team** total wins, loses and draws (as a list) for each matchup
# 1. get matchups for team 2. for each matchup, find if team is home or away 3. for each matchup, get w-l-d for home or away team 4. save it on a list? or dict

def getTeamwld(team : Team) -> list:
    matchup_list = team.schedule
    result_list = []

    for matchup in matchup_list:
        if team == matchup.home_team:
            key = matchup.away_team.team_name
            wins = matchup.home_team_live_score
            loses = matchup.away_team_live_score
            result_list.append((key,wins,loses))
        
        else:
            key = matchup.home_team.team_name
            wins = matchup.away_team_live_score
            loses = matchup.home_team_live_score
            result_list.append((key,wins,loses))
            
    return result_list