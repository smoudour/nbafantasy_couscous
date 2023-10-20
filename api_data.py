from espn_api.basketball import League

credentials = {'leagueID ' : 77307155,
               'year' : 2023,
               'espn_s2' : 'AECr6IlNrDvM6ry4e3hZr%2FKqQGTEEwJ7lca9n1NT9um64PDMGoEI2pg%2FWBQUcRM3TVQJ3qhbUYG7Xwxtvu1BdGEK92LL8LJ0d8P%2FYJTjOsISvhRhUz7BXEOHubjZV5sWpx9o%2B6sCbY%2BjyIWcIui3Xifrhdz%2BHf2bAFc6zPhMbXBJ3ToOlKxkmsYpgtri6uUUP3uBs81MCXLAGAjuvEInP63uCKtiqz0obRZ4jQv5EaMZyMbFZN%2FsxSbzNbzbOuY8L4oTUFt5yaw8w6AkMkTgm9VXjr5WkuhuGmob7xlwZbPRRA%3D%3D',
               'swid' : '6FCA26DA-B612-4F60-9544-7C58C0446928'}

my_league = League(league_id=credentials['leagueID '], year=credentials['year'], espn_s2=credentials['espn_s2'], swid=credentials['swid'])

# Global Variables
league_duration = 20
categories = ['PTS', 'BLK', 'STL', 'AST', 'REB', 'TO', '3PTM', 'FG%', 'FT%']