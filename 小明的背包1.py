
def get_data():
    n, max_w = map(int, input().split())
    w_value = []
    for _ in range(n):
        a, b = map(int, input().split())
        rate = b/a
        w_value.append((a, b, rate))
    #rate是性价比
    w_value.sort(key=lambda x: x[2])
    return n, max_w, w_value[::-1]

def get_best(max_w, w_value):
    dp = [0] * (max_w+1)
    for w, v, _ in w_value:
        for weight in range(max_w, w-1, -1):
            dp[weight] = max(dp[weight], dp[weight-w]+v)
    return dp[max_w]

if __name__ == "__main__":
    n, max_w, w_value = get_data()
    print(get_best(max_w, w_value))
    

    