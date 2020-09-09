
def count_hi(string):
    return string.count('hi')


def count_code(string):
    count = 0
    str_list = string.split('co')
    for i in str_list:
        if len(i) < 2:
            continue
        elif i[1] == 'e':
            count += 1
    return count
