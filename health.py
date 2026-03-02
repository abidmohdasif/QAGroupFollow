def take_damage(player, amount):
    return player - amount

def heal(player, amount):
    return player + amount

def is_alive(player):
    if player > 0:
        return True
    else:
        return False