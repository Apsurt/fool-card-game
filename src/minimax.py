def evaluate_early(player):
    result = 0
    for card in player.get_cards():
        result += card.value**2
        if card.is_trump:
            result += (card.value**2)*9
    return result/1000

def evaluate_late(player):
    return 7.3/(player.cards_left**2)

def maxn(depth, player_idx, game):
    if depth == 0:
        eval_tuple = []
        for p_idx in range(game.player_count):
            player_to_eval = game.get_player(p_idx)
            eval_tuple.append(evaluate_early(player_to_eval))
        eval_tuple = tuple(eval_tuple)
        return eval_tuple
    player = game.get_player(player_idx)

    best_defense = []
    best_attack = []
    best_eval = []

    possible_defense = []
    pass
    for pos_def in possible_defense:
        possible_attacks = []
        pass
        for pos_atk in possible_attacks:
            pass
