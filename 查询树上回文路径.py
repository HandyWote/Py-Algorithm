class Solution:
    """LeetCode 3041: Palindrome Path."""

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj: list[list[int]] = self.build(n, edges)
        chars: list[str] = list(s)

        log: int = max(1, n.bit_length())
        tin: list[int] = [0] * n
        tout: list[int] = [0] * n
        depth: list[int] = [0] * n
        parent: list[int] = [-1] * n
        pre0: list[int] = [0] * n

        timer: int = 0
        stack: list[tuple[int, int, int]] = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1
                char_mask: int = 1 << (ord(chars[u]) - ord("a"))
                pre0[u] = (
                    char_mask if p == -1 else pre0[p] ^ char_mask
                )
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        up: list[list[int]] = [parent]
        for _ in range(1, log):
            prev: list[int] = up[-1]
            cur: list[int] = [
                -1 if prev[v] == -1 else prev[prev[v]]
                for v in range(n)
            ]
            up.append(cur)

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff: int = depth[u] - depth[v]
            k: int = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1
            if u == v:
                return u
            for k in range(log - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return parent[u]

        bit: list[int] = [0] * (n + 2)

        def bit_add(idx: int, value: int) -> None:
            i: int = idx + 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def bit_get(idx: int) -> int:
            i: int = idx + 1
            result: int = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        for x in range(n):
            bit_add(tin[x], pre0[x])
            bit_add(tin[x] + 1, pre0[x])

        answer: list[bool] = []
        for command in queries:
            parts: list[str] = command.split()
            if parts[0] == "query":
                u: int = int(parts[1])
                v: int = int(parts[2])
                ancestor: int = lca(u, v)
                mask: int = (
                    bit_get(tin[u])
                    ^ bit_get(tin[v])
                    ^ (1 << (ord(chars[ancestor]) - ord("a")))
                )
                answer.append(self.is_palindrome(mask))
            else:
                idx: int = int(parts[1])
                new_ch: str = parts[2]
                old_ch: str = chars[idx]
                if old_ch != new_ch:
                    delta: int = (
                        (1 << (ord(old_ch) - ord("a")))
                        ^ (1 << (ord(new_ch) - ord("a")))
                    )
                    bit_add(tin[idx], delta)
                    bit_add(tout[idx] + 1, delta)
                    chars[idx] = new_ch

        return answer

    @staticmethod
    def build(n: int, edges: list[list[int]]) -> list[list[int]]:
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    @staticmethod
    def is_palindrome(mask: int) -> bool:
        return mask & (mask - 1) == 0
