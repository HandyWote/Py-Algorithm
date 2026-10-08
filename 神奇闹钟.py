import sys
input = sys.stdin.readline


format = "%Y-%m-%d %H:%M:%S"
from datetime import datetime, timedelta
START = datetime.strptime("1970-01-01 00:00:00", format)

def get_input():
    t = int(input())
    times = []
    for _ in range(t):
        y_m_d, h_m_s, gap = input().split()
        now_time = datetime.strptime(' '.join([y_m_d, h_m_s]), format)
        del y_m_d, h_m_s
        times.append([now_time, int(gap)])
    return times

def func(now_time: datetime, gap: int):
    delta = now_time - START
    delta_min = delta.total_seconds() // 60
    delta_min -= delta_min % gap
    alarm_time = START + timedelta(minutes=delta_min)
    return alarm_time

if __name__ == "__main__":
    times = get_input()
    for now_time, gap in times:
        print(func(now_time, gap).strftime(format))