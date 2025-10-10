def prime_generator():
    """素数を順番に生成するジェネレータ"""
    n = 2
    primes = []
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1

a = int(input("数字を入力: "))

original_a = a  # 元の数字を保存

# 素因数分解
factors = []  # (素数, 指数) のタプルを入れる
gen = prime_generator()  # ジェネレータを1つだけ作る

while a > 1:
    prime = next(gen)
    count = 0
    while a % prime == 0:
        a = a // prime  # 整数割り算
        count += 1
    if count > 0:
        factors.append((prime, count))

# 出力
print(f"{original_a} の素因数分解結果:")
for i, (prime, exponent) in enumerate(factors):
    end_char = " + " if i < len(factors) - 1 else ""#末尾は+なし
    print(f"{prime}^{exponent}", end=end_char)
print()  # 最後の改行
