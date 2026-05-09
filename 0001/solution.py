def encrypt(toencrypt):
    step1 = toencrypt[::-1]

    step2list = []
    for i in range(len(step1)):
        if step1[i] == "a":
            step2list.append("0")
        elif step1[i] == "e":
            step2list.append("1")
        elif step1[i] == "i":
            step2list.append("2")
        elif step1[i] == "o":
            step2list.append("2")
        elif step1[i] == "u":
            step2list.append("3")
        else:
            step2list.append(step1[i])

    step2 = "".join(step2list)
    step3 = step2 + "aca"

    return step3

if __name__ == "__main__":
    toencrypt = input("what to encrypt? ").lower()
    print(encrypt(toencrypt))
