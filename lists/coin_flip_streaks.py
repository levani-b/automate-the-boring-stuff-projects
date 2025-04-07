import random


def find_streak(coin_flips, streak_length):
    count = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            count += 1
            if count == streak_length:
                return  True
        else:
            count = 1
    return False


def main():
    number_of_streaks = 0
    streak_length = 6
    num_experiments = 10000
    num_flips = 100

    for experiment_number in range(num_experiments):
        coin_flips = []
        for i in range(num_flips):
            flip = random.randint(0,1)
            if flip == 0:
                coin_flips.append('H')
            else:
                coin_flips.append('T')

        if find_streak(coin_flips, streak_length):
            number_of_streaks += 1

    chance_of_streak = (number_of_streaks / num_experiments) * 100
    print('Chance of streak: %s%%' % chance_of_streak)


if __name__ == "__main__":
    main()