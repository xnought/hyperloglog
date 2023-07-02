import hashlib


# todo use bit operations for wayyyyyyy faster performance
def num_leading_zeros(num):
    str_bin = bin(num)[2:]
    count = 0
    for c in reversed(str_bin):
        if c == "0":
            count += 1
        else:
            break
    return count


# todo use a better hash function for hyperloglog
def hasher(item):
    return int(hashlib.md5(f"{str(item)}".encode()).hexdigest(), 16)


def hyperloglog(data):
    max_zeroes = 0
    for d in data:
        hash = hasher(d)
        max_zeroes = max(max_zeroes, num_leading_zeros(hash))

    return 2 ** (max_zeroes + 1)


def cardinality_hashmap(data):
    map = {}
    for d in data:
        if d in map:
            map[d] += 1
        else:
            map[d] = 1

    return len(map)


def generate_data(cardinality=100, length=1000):
    import random

    data = []
    for i in range(length):
        data.append(random.randint(0, cardinality))

    return data


def main():
    data = generate_data(25_000, 100_000_000)

    # print(cardinality_hashmap(data))
    print(hyperloglog(data))


if __name__ == "__main__":
    main()
