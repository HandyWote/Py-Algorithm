def print_2025(h, w):
    s = '2025' * 200
    for i in range(h):
        print(s[i:i+w])

if __name__ == '__main__':
    h, w = map(int, input().split())
    print_2025(h, w)