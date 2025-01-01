cost = []
hand = 0
bank = 0
for i in range(12):
    cost.append(int(input()))
for i in range(12):
    hand += 300
    if hand >= cost[i] + 100:
        save = hand - cost[i]
        save -= save % 100
        bank += save
        hand -= save
    hand -= cost[i]
    if hand < 0:
        print(f"-{i+1}")
        break
else:
    hand += bank * 1.2
    print(int(hand))