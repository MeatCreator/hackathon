def __init__(self, player_health, enemy_health):
    self.player_health = player_health
    self.enemy_health = enemy_health


# subtract damage from health
# damage will be set to 1
# first boss will have 1 health,
# second will have 2,
# final will have 3
# player has 2

def strike(health, extradamage = 0) -> int:
    return health - (extradamage + 1)

