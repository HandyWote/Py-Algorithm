from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from typing import List


class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_q = deque()
        self.packet_set = set()
        self.dest_to_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        
        self.packet_set.add(packet)

        if len(self.packet_q) == self.memory_limit:
            self.forwardPacket()
        
        self.packet_q.append(packet)
        self.dest_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_q:
            return []
        
        packet = self.packet_q.popleft()
        self.packet_set.remove(packet)
        self.dest_to_timestamps[packet[1]].popleft()

        if not self.dest_to_timestamps[packet[1]]:
            del self.dest_to_timestamps[packet[1]]
        
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_to_timestamps:
            return 0
        
        timestamps = list(self.dest_to_timestamps[destination])
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

# class Router:

#     def __init__(self, memoryLimit: int):
#         self.size = memoryLimit
#         self.que = Deque()
#         self.seen = set()
#         self.destination = defaultdict(SortedList) #[None for _ in range(2 * 10**5 + 1)]

#     def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
#         if (source, destination, timestamp) in self.seen:
#             return False
#         if self.size == len(self.que):
#             self.forwardPacket()
#         # if self.destination[destination] == None:
#         #     self.destination[destination] = SortedList()
#         self.seen.add((source, destination, timestamp))
#         self.destination[destination].add(timestamp)
#         self.que.append((source, destination, timestamp))
#         return True

#     def forwardPacket(self) -> List[int]:
#         if len(self.que) == 0:
#             return []
#         (s, d, t) = self.que.popleft()
#         self.destination[d].remove(t)
#         self.seen.discard((s,d,t))
#         return [s, d, t]

#     def getCount(self, destination: int, startTime: int, endTime: int) -> int:
#         if destination not in  self.destination:
#             return 0
#         idx1 = self.destination[destination].bisect_left(startTime)
#         idx2 = self.destination[destination].bisect_right(endTime)
#         return idx2 - idx1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)