# Сколько минимально требуется шагов чтобы уравнять массив длиной n, совершая операции над n - 1 элементами?
# Операции: прибавление 5, 2, 1


def count_counter(last_el, cur_el):
    print(last_el, cur_el)
    diff = abs(last_el - cur_el)
    i = diff // 5
    j = (diff - 5 * i) // 2
    k = diff - 5 * i - 2 * j
    return i, j, k, min(last_el, cur_el) + 5 * i + 2 * j + k


def count_ops():
    if len(arr) < 2:
        return 0
    i, j, k, last_el = count_counter(arr[0], arr[1])
    counter = i + j + k
    to_add = 5 * i + 2 * j + k
    for m in range(2, len(arr)):
        i, j, k, last_el = count_counter(last_el, arr[m] + to_add)
        to_add = 5 * i + 2 * j + k
        counter += i + j + k
    return counter


if __name__ == '__main__':
    arr = [0, 0, 5]
    print(count_ops())
