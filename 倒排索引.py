import sys

input = sys.stdin.readline

def get_input(n: int):
    d = []
    for _ in range(n):
        d.append(input().strip())
    q = input().strip()
    return d, q

def Ngram(s: str):
    index = set()
    for windows_length in range(MIN, MAX+1):
        window = list(s[:windows_length])
        index.add(''.join(window))
        for i in s[windows_length:]:
            window.pop(0)
            window.append(i)
            index.add(''.join(window))
    return index


if __name__ == "__main__":
    n, MIN, MAX = map(int, input().split())
    d, q = get_input(n)
    ans = 0
    q_Ngram = Ngram(q)
    for doc in d:
        doc_Ngram = Ngram(doc)
        if q_Ngram & doc_Ngram: ans += 1
    print(ans)
