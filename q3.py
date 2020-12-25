def make_change(amount, coins):
    to_make = amount
    change_amts = []
    for i in range(len(coins)):
        # What's the max number of coins we can take?
        num_coins = to_make // coins[i]

        # Leftover after taking away max coins
        to_make = to_make % coins[i]

        if num_coins > 0:
            change_amts.append(str(num_coins) + ' x ' + str(coins[i]))

    # If we cannot make the amount or nothing to make, then print the message
    if to_make > 0 or len(change_amts) == 0:
        print('Sorry. Change not available')
    else:
        # Otherwise, print the coins and amounts
        print('Amount: ' + str(amount))
        for amt in change_amts:
            print(amt)

make_change(1366, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(512, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(9, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(999, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(1689, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(0, [1000, 500, 100, 50, 20, 10, 5, 2, 1])
make_change(1689, [1000, 500, 100, 50, 10, 2, 1])
make_change(89, [1000, 500, 100, 50, 20, 10, 5, 2])