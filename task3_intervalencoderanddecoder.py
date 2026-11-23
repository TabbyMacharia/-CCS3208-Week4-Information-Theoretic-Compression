model = {
    "A": (0.0, 0.5),
    "B": (0.5, 0.8),
    "C": (0.8, 1.0)
}


def encode_interval(message, model):
  low, high = 0.0, 1.0
  trace = []
  for symbol in message:
     a, b = model[symbol]
     width = high - low
     low, high = low + width * a, low + width * b
     trace.append((symbol, low, high))
  return low, high, trace

def decode_tag(tag, length, model):
  low, high = 0.0, 1.0
  result = []
  for _ in range(length):
    width = high - low
    for symbol, (a, b) in model.items():
       next_low = low + width * a
       next_high = low + width * b
       if next_low <= tag < next_high:
          result.append(symbol)
          low, high = next_low, next_high
          break
    else:
      raise ValueError("Tag outside modeled intervals")
  return "".join(result)

message = "BA"
low, high, trace = encode_interval(message, model)
tag = (low + high) / 2
print("Trace:", trace)
print("Final interval:", (low, high), "tag:", tag)
print("Decoded:", decode_tag(tag, len(message), model))
