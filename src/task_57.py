import sys
import itertools

def calculate(num_list, ops): #四則演算を行う
    result = num_list[0]
    for i in range(3):#3回演算する
        if ops[i] == '+':
            result += num_list[i + 1]
        elif ops[i] == '-':
            result -= num_list[i + 1]
        elif ops[i] == '*':
            result *= num_list[i + 1]
        elif ops[i] == '/':
            if num_list[i + 1] == 0:
                return None  # ゼロ除算を回避
            result /= num_list[i + 1]
    return result

def find_combinations(nums):#10になる組み合わせの探索
    operators = ['+', '-', '*', '/']
    for perm in itertools.permutations(nums):#数字の順列
        for ops in itertools.product(operators, repeat=3):#演算子の組み合わせ
            if calculate(perm, ops) == 10:
                print(f"{perm[0]} {ops[0]} {perm[1]} {ops[1]} {perm[2]} {ops[2]} {perm[3]} = 10")#結果出力

# コマンドライン引数から4つの整数を取得
numbers = list(map(int, sys.argv[1:5]))
find_combinations(numbers)