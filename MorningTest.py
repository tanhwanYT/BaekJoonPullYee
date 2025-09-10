a = int(input())
coins = []

def gusremdon(n, coins):
    return gusremdon(n,coins[1:]) +gusremdon(amount-coins[0],coins)

return 