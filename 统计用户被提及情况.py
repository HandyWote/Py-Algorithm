from collections import defaultdict


class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        ans = [0] * numberOfUsers
        # 设计一个字典，记录每个用户的离线时间{用户ID)(id<int>): 离线时间戳(int)}
        offline_timestamp = defaultdict(int)
        # 修改排序逻辑：主要按时间戳排序，时间相同时OFFLINE优先于MESSAGE
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        for event in events:
            if event[0] == "MESSAGE":
                timestamp = int(event[1])
                mentioned_users = event[2].split()
                if "ALL" in mentioned_users:
                    for user_id in range(numberOfUsers):
                        ans[user_id] += 1
                elif "HERE" in mentioned_users:
                    for user_id in range(numberOfUsers):
                        if offline_timestamp[user_id] == 0 or (offline_timestamp[user_id]!=0 and offline_timestamp[user_id]+60 <= timestamp):
                            ans[user_id] += 1
                else:
                    for user in mentioned_users:
                        user_id = int(user[2:])  # 提取用户ID
                        ans[user_id] += 1

            else:  # OFFLINE
                timestamp = int(event[1])
                user_id = int(event[2])
                offline_timestamp[user_id] = timestamp
        return ans

if __name__ == "__main__":
    from test import Test, Case
    cases = Case()
    cases.add_cases(
        (
            ((2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]), [2,2]),
            ((2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]), [2,2]),
            ((2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]), [0, 1]),
            ((3, [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]), [1,0,2])
        )
    )
    Test(cases, Solution(), 'countMentions').run()