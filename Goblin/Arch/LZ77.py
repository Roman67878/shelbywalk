def lz77_compress(text, window_size):
    result = []
    pos = 0

    while pos < len(text):
        max_match_len = 0
        best_match = (0, 0)

        for i in range(1, window_size + 1):
            if pos - i < 0:
                break

            match_len = 0
            while match_len < len(text) - pos and text[pos - i + match_len] == text[pos + match_len]:
                match_len += 1

            if match_len > max_match_len:
                max_match_len = match_len
                best_match = (i, match_len)

        if best_match[1] > 0:
            result.append(best_match)
            pos += best_match[1] + 1
        else:
            result.append((0, 0, text[pos]))
            pos += 1

    return result


text = "abcdefabcdefabcdefabcdef"
window_size = 0
compressed_text = lz77_compress(text, window_size)
print(compressed_text)
