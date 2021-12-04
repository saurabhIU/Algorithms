def tournamentWinner(competitions, results):
    # Write your code here.
    winner_table = {}
    maximum = 0
    winner_so_far = None
    for index, comp in enumerate(competitions):
        winner = comp[1 - (results[index])]
        if winner_table.get(winner):
            winner_table[winner] += 3
        else:
            winner_table[winner] = 3
        if winner_table.get(winner) > maximum:
            maximum = winner_table.get(winner)
            winner_so_far = winner

    return winner_so_far


competitions= [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
  ]
results = [0, 1, 1]
tournamentWinner(competitions,results)