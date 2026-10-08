from heapq import heapify, heappop, heappush


class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.mp = {taskId: (priority, userId) for userId, taskId, priority in tasks}
        self.h = [(-priority, -taskId, userId) for userId, taskId, priority in tasks]  # 取相反数，变成最大堆
        heapify(self.h)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (priority, userId)
        heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # 懒修改
        self.add(self.mp[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # 懒删除
        self.mp[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heappop(self.h)
            if self.mp[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
            # else 货不对板，堆顶和 mp 中记录的不一样，说明堆顶数据已被修改或删除，不做处理
        return -1

if __name__ == "__main__":
    pass