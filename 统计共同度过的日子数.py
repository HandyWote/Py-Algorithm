from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        times: list[datetime] = self.parse([arriveAlice, arriveBob, leaveAlice, leaveBob])
        days: int = (min(times[2:]) - max(times[:2])).days + 1
        return days if days > 0 else 0


    @staticmethod
    def parse(times: list[str]) -> list[datetime]:
        return [datetime.strptime(s, "%m-%d") for s in times]

if __name__ == "__main__":
    s = Solution()
    print(s. countDaysTogether("10-15", "10-18", "10-16", "10-19"))
