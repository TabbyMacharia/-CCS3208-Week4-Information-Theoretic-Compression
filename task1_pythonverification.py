from collections import Counter
from math import log2

message = "AAAAAABBBCCD"
freq = Counter(message)
n = len(message)
prob = {s: f / n for s, f in sorted(freq.items())}
entropy = -sum(v * log2(v) for v in prob.values())
for s, v in prob.items():
  print(s, "freq=", freq[s], "p=", round(v, 4),
       "I=", round(-log2(v), 4))
print("Entropy:", round(entropy, 4), "bits/symbol")
print("Fixed length:", n * 2, "bits")
