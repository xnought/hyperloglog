import mmh3
from tqdm import tqdm


def num_leading_zeros(num):
    bits = num.bit_length()
    # iterate over each bit from right to left
    # stop when found a 1
    for i in range(bits):
        if num & (1 << i):
            return i
    return bits


def hasher(item):
    return mmh3.hash(str(item), signed=False)


def hyperloglog(data, log_progress=False):
    max_zeros = 0
    for d in tqdm(data, total=len(data), disable=not log_progress):
        hash = hasher(d)
        max_zeros = max(max_zeros, num_leading_zeros(hash))

    return 2 ** (max_zeros + 1)


def generate_data(cardinality=100, length=1000):
    import random

    data = []
    for _ in range(length):
        data.append(random.randint(0, cardinality))

    return data


def main():
    length = 100_000_00
    cardinality = 100_000
    data = generate_data(cardinality, length)
    print(
        "estimated cardinality",
        hyperloglog(data, log_progress=True),
        "vs. actual",
        cardinality,
    )


if __name__ == "__main__":
    main()
