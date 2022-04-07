def two_d_arr():
    flag = 0
    for iteration_value in range(0, 10):
        min_limit = iteration_value * 100
        max_limit = 100*(iteration_value + 1)
        for number in range(min_limit, max_limit+1):
            if number > 1:
                for iterating_number in range(2, number):
                    if number % iterating_number == 0:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag == 1:
                    if number not in list1:
                        list1.append(number)
        # print("Prime number in range ", min, "-", max, "=", list1)
        list0.append(min_limit)
        list0.append(max_limit)
        array[0] = list0
        array[1][0] = list1
        print(array)
        list0.clear()
        list1.clear()


if __name__ == "__main__":
    list1 = []
    array = [[], [[]]]
    list0 = []
    two_d_arr()
