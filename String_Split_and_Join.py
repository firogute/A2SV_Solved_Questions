def split_and_join(line):
    # write your code here
    new_str_lst = line.split(" ")
    return "-".join(new_str_lst)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
