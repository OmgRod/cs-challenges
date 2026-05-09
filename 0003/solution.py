def move(phrase):
    new_phrase = ""
    for i in range(len(phrase)):
        # i'm aware this code increments ALL characters
        # codes by 1 so it may be a bit broken depending
        # on the input
        new_phrase += chr(ord(phrase[i]) + 1)
    return new_phrase

if __name__ == "__main__":
    print("ORIGINAL: ", "hello bye welcome")
    print("ENCRYPTED: ", move("hello bye welcome"))
