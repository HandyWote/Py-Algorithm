from functools import cmp_to_key


if __name__ == "__main__":
    n = int(input())
    nums = [bin(i)[2::] for i in range(1, n+1)]
    nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
    print(int("".join(nums), 2))
