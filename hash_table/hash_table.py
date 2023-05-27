import sys


class HashTableNode:

    def __init__(self, key=None):
        self.key = key
        self.is_deleted = False


class HashTable:

    def __init__(self):
        self._load_factor_limit = 0.75
        self.HASH1 = 11
        self.HASH2 = 13

        self._start_num = 8
        self._array = [None for _ in range(self._start_num)]

        self.cur_size = 0
        self.cur_array_size = self._start_num

    def get_hash1(self, key_arr, size):
        hash_value = 0
        for i in range(len(key_arr) - 1, -1, -1):
            hash_value += (self.HASH1 * hash_value + ord(key_arr[i])) % size
        return hash_value % size

    def get_hash2(self, key_arr, size):
        hash_value = 0
        for i in range(len(key_arr) - 1, -1, -1):
            hash_value += (self.HASH2 * hash_value + ord(key_arr[i])) % size
        return (hash_value * 2 + 1) % size

    def rehash(self):
        new_size = 2 * self.cur_array_size
        new_array = [None for _ in range(new_size)]

        for i in range(self.cur_array_size):
            if self._array[i] is not None and not self._array[i].is_deleted:
                h1 = self.get_hash1(self._array[i].key, new_size)
                h2 = self.get_hash2(self._array[i].key, new_size)
                k = 0

                while new_array[h1] is not None and k < new_size:
                    h1 = (h1 + h2) % new_size
                    k += 1

                new_array[h1] = self._array[i]

            self._array[i] = None
        self._array = new_array
        self.cur_array_size = new_size

    def add(self, key_value):
        if self.cur_size / self.cur_array_size >= self._load_factor_limit:
            self.rehash()

        h1 = self.get_hash1(key_value, self.cur_array_size)
        h2 = self.get_hash2(key_value, self.cur_array_size)

        i = 0
        first_deleted_elem = -1

        while self._array[h1] is not None and i < self.cur_array_size:
            if self._array[h1].key == key_value and not self._array[h1].is_deleted:
                return

            if self._array[h1].is_deleted and first_deleted_elem < 0:
                first_deleted_elem = h1

            h1 = (h1 + h2) % self.cur_array_size
            i += 1

        if first_deleted_elem < 0:
            self._array[h1] = HashTableNode(key_value)

        else:
            self._array[first_deleted_elem].key = key_value
            self._array[first_deleted_elem].is_deleted = False

        self.cur_size += 1

    def remove(self, key_value):
        h1 = self.get_hash1(key_value, self.cur_array_size)
        h2 = self.get_hash2(key_value, self.cur_array_size)
        i = 0
        while self._array[h1] is not None and i < self.cur_array_size:
            if self._array[h1].key == key_value and not self._array[h1].is_deleted:
                self._array[h1].is_deleted = True
                self.cur_size -= 1
                return True
            h1 = (h1 + h2) % self.cur_array_size
            i += 1

        return False

    def has(self, key_value):
        h1 = self.get_hash1(key_value, self.cur_array_size)
        h2 = self.get_hash2(key_value, self.cur_array_size)
        i = 0

        while self._array[h1] is not None and i < self.cur_array_size:
            if self._array[h1].key == key_value and not self._array[h1].is_deleted:
                return True

            h1 = (h1 + h2) % self.cur_array_size
            i += 1

        return False


def main():
    hash_table = HashTable()
    for line in sys.stdin:
        line = line.strip()
        command, value = line.split()
        if command == '+':
            if hash_table.has(value):
                print('FAIL')
            else:
                print('OK')
                hash_table.add(value)

        elif command == '-':
            if hash_table.has(value):
                print('OK')
                hash_table.remove(value)
            else:
                print('FAIL')

        else:
            if hash_table.has(value):
                print('OK')
            else:
                print('FAIL')


if __name__ == '__main__':
    main()
