import random


cnt = 0
for _ in range(1000):
    val = [random.uniform(0, 1) for _ in range(16)]
    val = sum(val) / 16
    if val - 0.5 > 0.5 or val - 0.5 < -0.5:
        cnt += 1
print(cnt / 1000)
# 0.0