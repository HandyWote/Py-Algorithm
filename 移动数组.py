import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, q = int(data[idx]), int(data[idx + 1]); idx += 2
    a = [int(data[i]) for i in range(idx, idx + n)]; idx += n
    offset = 0
    for i in range(idx, idx + q):
        if data[i] == b'2': offset -= 1
        else: offset += 1
    offset %= n
    print(' '.join(map(str, a[offset:] + a[:offset])))

if __name__ == '__main__':
    main()
