from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n: int = len(parent)
        tree: defaultdict[int, list[int]] = defaultdict(list)
        record: defaultdict[str, list[int]] = defaultdict(list)
        ans: list[int] = [0] * n

        for i in range(1, n):
            tree[parent[i]].append(i)

        def search(node_index: int) -> None:
            ans[node_index] += 1
            record[s[node_index]].append(node_index)
            for res_node_index in tree[node_index]:
                search(res_node_index)
                ans[record[s[res_node_index]][-1] if record[s[res_node_index]] else node_index] += ans[res_node_index]
            record[s[node_index]].pop()

        search(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findSubtreeSizes([-1,0,0,1,1,1], "abaabc"))
