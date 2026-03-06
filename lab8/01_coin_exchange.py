def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    coins = convert_key(json.loads(input()))
    print(f"Amount: {amount}")

    result = {}
    for coins_value, coins_amount in coins.items():
        required = amount // coins_value

        result[coins_value] = min(required, coins_amount)
        amount -= coins_value * result[coins_value]

    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")

        for coin, amount in result.items():
            print(f"  {coin} baht = {amount} coins")

        print(f"Number of coins: {sum(result.values())}")

main()