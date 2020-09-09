    
def gami_s(num):
    n_list = [1]
    for a in range(num):
        result = []
        count = 0
        i = 0
        while i < len(n_list) -1:
            if i == 0:
                i += 1
                count = 1

            elif n_list[i] == n_list[i - 1]:
                i += 1
                count += 1

            else:
                result.append(n_list[i- 1])
                result.append(count)
                i += 1
                count = 1

        if n_list[i] == n_list[i -1]:
            count += 1
            result.append(n_list[i])
            result.append(count)
        else:
            result.append(n_list[i-1])
            result.append(count)
            result.append(n_list[i])
            result.append(1)
        n_list = result
        print(result)
        print('{0:=^40}'.format('구분선'))
        
def gami_f(num):
    n_list = [1]
    for a in range(num):
        result = []
        count = 0
        i = 0
        while i < len(n_list) -1:
            if i == 0:
                i += 1
                count = 1

            elif n_list[i] == n_list[i - 1]:
                i += 1
                count += 1

            else:
                result.append(n_list[i- 1])
                result.append(count)
                i += 1
                count = 1

        if n_list[i] == n_list[i -1]:
            count += 1
            result.append(n_list[i])
            result.append(count)
        else:
            result.append(n_list[i-1])
            result.append(count)
            result.append(n_list[i])
            result.append(1)
        n_list = result
    print(result)
