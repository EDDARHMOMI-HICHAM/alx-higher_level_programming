def remove_char_at(str, n):
    if 0 <= n < len(str):
        new_str = ""
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
        return new_str
    return str
