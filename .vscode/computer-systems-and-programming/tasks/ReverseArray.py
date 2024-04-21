def reverse_array(text):
    start = 0
    end = len(text) - 1
    while start < end:
        text[start], text[end] = text[end], text[start]
        start += 1
        end -= 1
    return text

def main():
    some_text = ["Some", "text", "to", "revert"]
    result = reverse_array(some_text)
    print(result)

if __name__ == "__main__":
    main()
