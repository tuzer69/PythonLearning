players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_players = []
for one, two in players.items():
	new_players.append(one + two)
print(new_players)
