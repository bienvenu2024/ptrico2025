def count_ways_to_sum(total, num_dice, dice_faces=6, memo=None):
    if memo is None:
        memo = {}

        if total == 0 and num_dice == 0:
            return 1
        if total < 0 or num_dice == 0:
            return 0

        if(total, num_dice) in memo:
            return memo[(total, num_dice)]

        ways = 0
        for face in range(1, dice_faces + 1):
            ways += count_ways_to_sum(total - face, num_dice - 1, dice_faces, memo)

    memo[(total, num_dice)] = ways
    return ways
    result = count_ways_to_sum(20, 5)
    print(f"nombre de façon d'obtenir une somme de 20 avec 5 dés à 6 faces:{result}")
