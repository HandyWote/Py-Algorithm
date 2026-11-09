from collections.abc import Iterator
import bisect
import heapq
from typing import final


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        router: Router = Router(k)

        for i, (time, take) in enumerate(zip(arrival, load)):
            router.route(i, time, take)

        max_cnt: int = max(s.work_cnt for s in router)
        return [s.id for s in router if s.work_cnt == max_cnt]


@final
class Server:
    __slots__ = ("id", "valid_time", "work_cnt")

    def __init__(self, sid: int) -> None:
        self.id: int = sid
        self.valid_time: int = 0
        self.work_cnt: int = 0

    def accept(self, time: int, take: int) -> None:
        self.work_cnt += 1
        self.valid_time = time + take

    def __lt__(self, other: "Server") -> bool:
        return self.valid_time < other.valid_time


@final
class Router:
    __slots__ = ('servers', 'busy', 'free')

    def __init__(self, k: int) -> None:
        self.servers: list[Server] = [Server(i) for i in range(k)]
        self.busy: list[Server] = []
        self.free: list[int] = list(range(k))

    def route(self, index: int, time: int, take: int) -> None:
        self._release(time)
        
        if not self.free: return None
        
        sid: int = self._pick(self.free, index % len(self.servers))
        server: Server = self.servers[sid]
        server.accept(time, take)
        heapq.heappush(self.busy, server)

    def _release(self, now: int) -> None:
        while self.busy and self.busy[0].valid_time <= now:
            finished: Server = heapq.heappop(self.busy)
            bisect.insort(self.free, finished.id)
    
    @staticmethod
    def _pick(free: list[int], target: int) -> int:
        pos: int = bisect.bisect_left(free, target)
        if pos == len(free):
            pos = 0
        return free.pop(pos)

    def __iter__(self) -> Iterator[Server]:
        return iter(self.servers)
