class Solution:
    """LeetCode 301: Remove Invalid Parentheses.

    Remove the minimum number of invalid parentheses so the result is a valid
    string. Return every distinct valid string obtainable with that minimum.

    Strategy:
        1. One left-to-right scan determines the minimum number of '(' and ')'
           that must be removed for validity (a theoretical lower bound).
        2. A depth-first backtracking search enumerates, for each character,
           the choice of keeping or deleting it — pruning branches that can
           no longer reach that lower bound.
        3. A set deduplicates results produced by different deletion paths.
    """

    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem, right_rem = self._min_removals(s)
        results: set[str] = set()
        n = len(s)

        def backtrack(
            index: int,
            left_rem: int,
            right_rem: int,
            open_count: int,
            path: str,
        ) -> None:
            # Prune: deletion budget cannot go negative.
            if left_rem < 0 or right_rem < 0:
                return

            # Prune: remaining characters insufficient to satisfy deletions.
            if n - index < left_rem + right_rem:
                return

            # Leaf: all characters consumed; accept iff fully valid.
            if index == n:
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    results.add(path)
                return

            ch = s[index]

            if ch == '(':
                backtrack(index + 1, left_rem - 1, right_rem, open_count, path)
                backtrack(index + 1, left_rem, right_rem, open_count + 1, path + ch)

            elif ch == ')':
                backtrack(index + 1, left_rem, right_rem - 1, open_count, path)
                if open_count > 0:
                    backtrack(index + 1, left_rem, right_rem, open_count - 1, path + ch)

            else:
                backtrack(index + 1, left_rem, right_rem, open_count, path + ch)

        backtrack(0, left_rem, right_rem, 0, "")
        return list(results)

    @staticmethod
    def _min_removals(s: str) -> tuple[int, int]:
        """Return (left_rem, right_rem): minimum surplus '(' and ')'.

        Matches each ')' with a pending '(' when possible; otherwise counts it
        as surplus. Any '(' still pending at the end is also surplus.

        Time: O(n). Space: O(1).
        """
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        return left_rem, right_rem
