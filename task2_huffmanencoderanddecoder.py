
from collections import Counter
import heapq
from itertools import count

def huffman_codes(text):
  frequencies = Counter(text)
  serial = count()
  heap = [(f, next(serial), s) for s, f in frequencies.items()]
  heapq.heapify(heap)
  if len(heap) == 1:
      return {text[0]: "0"}
  while len(heap) > 1:
      f1, _, left = heapq.heappop(heap)
      f2, _, right = heapq.heappop(heap)
      heapq.heappush(heap, (f1 + f2, next(serial), (left, right)))
  root = heap[0][2]
  codes = {}
  def walk(node, prefix):
      if isinstance(node, str):
          codes[node] = prefix
      else:
          walk(node[0], prefix + "0")
          walk(node[1], prefix + "1")
  walk(root, "")
  return codes

def decode_bits(bits, codes):
  reverse = {v: k for k, v in codes.items()}
  output, buffer = [], ""
  for bit in bits:
    buffer += bit
    if buffer in reverse:
       output.append(reverse[buffer])
       buffer = ""
  assert buffer == "", "Incomplete bitstream"
  return "".join(output)

def is_prefix_free(codes):
    codewords = list(codes.values())

    for i in range(len(codewords)):
        for j in range(len(codewords)):
            if i != j and codewords[j].startswith(codewords[i]):
                return False

    return True

def average_code_length(codes, frequencies):
    total_bits = 0
    total_symbols = 0

    for symbol, frequency in frequencies.items():
        code_length = len(codes[symbol])
        total_bits += frequency * code_length
        total_symbols += frequency

    return total_bits / total_symbols

source = "A" * 45 + "B" * 13 + "C" * 12 + "D" * 10

codes = huffman_codes(source)
message = "ABACD"
bits = "".join(codes[ch] for ch in message)
print("Codes:", codes)
print("Encoded:", bits, "length:", len(bits))
print("Decoded:", decode_bits(bits, codes))
assert decode_bits(bits, codes) == message
print("Prefix-free:", is_prefix_free(codes))
print("Average code length:", average_code_length(codes, Counter(source)))


message2 = "AABACAD"

bits2 = "".join(codes[ch] for ch in message2)

decoded2 = decode_bits(bits2, codes)

print("Second message:", message2)
print("Second encoded:", bits2)
print("Second encoded length:", len(bits2))
print("Second decoded:", decoded2)

assert decoded2 == message2
