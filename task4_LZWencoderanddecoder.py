
def lzw_encode(data, alphabet="AB"):
    dictionary = {s: i + 1 for i, s in enumerate(alphabet)}
    next_code = len(dictionary) + 1
    output, w, additions = [], "", []

    for k in data:
        if w + k in dictionary:
            w += k
        else:
            output.append(dictionary[w])
            dictionary[w + k] = next_code
            additions.append((next_code, w + k))
            next_code += 1
            w = k

    if w:
        output.append(dictionary[w])

    return output, additions


def lzw_decode(codes, alphabet="AB"):
    dictionary = {i + 1: s for i, s in enumerate(alphabet)}
    next_code = len(dictionary) + 1

    if not codes:
        return ""

    w = dictionary[codes[0]]
    result = [w]

    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Invalid LZW code")

        result.append(entry)
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry

    return "".join(result)


for text in ("ABABABA", "ABABABABA", "AAAAAAAABBBBBBBB"):
    codes, additions = lzw_encode(text)
    recovered = lzw_decode(codes)

    print(text, "->", codes, "->", recovered)
    print("New entries:", additions)

    assert recovered == text
