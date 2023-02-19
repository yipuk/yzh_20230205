

# coins with face values of 1 pence, 2, 5, 10, 20, 50 pences, 1 and 2 pounds
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
N = len(COINS)


def convert_amount_string_to_interger(amount_string):
    try:
        amount_string = amount_string.replace('£', '')
        amount_list = amount_string.split('-')
        if amount_list[1] == '':
            amount_list[1] = '0'
        if len(amount_list[1]) <= 2:
            return int(amount_list[0]) * 100 + int(amount_list[1])
    except:
        raise ValueError("The input string must be in the format of £{pound}-{pence}.")


def coin_machine_all_combinations(amount_string):

    amount = convert_amount_string_to_interger(amount_string)
    count = [1] + [0] * amount
    for i in range(N-1, -1, -1):

        next_count = [1] + [0] * amount
        for j in range(1, amount + 1):

            next_count[j] = count[j]
            if j - COINS[i] >= 0:
                next_count[j] += next_count[j - COINS[i]]

        count = next_count

    return count[amount]


def coin_machine_odd_number_of_combinations(amount_string):

    amount = convert_amount_string_to_interger(amount_string)
    count_odd = [0] + [0] * amount
    count_even = [1] + [0] * amount

    for i in range(N-1, -1, -1):

        next_count_odd = [0] + [0] * amount
        next_count_even = [1] + [0] * amount
        for j in range(1, amount + 1):

            next_count_odd[j] = count_odd[j]
            next_count_even[j] = count_even[j]
            if j - COINS[i] >= 0:
                next_count_odd[j] += next_count_even[j - COINS[i]]
                next_count_even[j] += next_count_odd[j - COINS[i]]

        count_odd = next_count_odd
        count_even = next_count_even

    return count_odd[amount]


x = "£100-"
z = coin_machine_odd_number_of_combinations(x)
print(z)