def make_hash_table(size):
    hash_table = {}
    for i in range(size):
        hash_table[i] = []
    return hash_table


def hash_fn(input, hash_table_size):
    return len(input) % hash_table_size


def main(array, hash_table_size):
    hash_table = make_hash_table(hash_table_size)
    for item in array:
        index = hash_fn(item, hash_table_size)
        hash_table[index].append(item)
    return hash_table


array = ["apple", "boy", "cat", "dog", "elephant", "fish", "grapes", "horse",
         "jug", "king", "lion", "mango", "next", "orange", "peacock", "queen",
         "rabbit"]


print main(array, 10)
