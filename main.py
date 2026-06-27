import json

with open('player_stats.json', 'r') as ps:
    data = json.load(ps)

print(data)

def fieldgoals_percentage(player_id, points):
    keys = {1: "FT", 2: "2FG", 3: "3FG"}
    key = keys.get(points)
    for player in data:
        if player.get('player_id') == player_id:
            target_stat = player.get('stats').get(key)
            attempts = target_stat.get('attempts')
            made = target_stat.get('made')

            if attempts == 0:
                return 0
            else:
                return (made/attempts)*100
    return "Player not found"

x = fieldgoals_percentage(1,3)
print(f"Porcentaje: {x}%")