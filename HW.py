import types
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list_index = 0
        self.current_element_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.list_of_list):
            raise StopIteration
        current_list = self.list_of_list[self.current_list_index]
        if self.current_element_index >= len(current_list):
            self.current_list_index += 1
            self.current_element_index = 0
            return next(self)
        else:
            element = current_list[self.current_element_index]
            self.current_element_index += 1
            return element


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


test_1()

def flat_generator(list_of_lists):
    current_list_index = 0
    current_element_index = 0

    while current_list_index < len(list_of_lists):
        current_list = list_of_lists[current_list_index]
        if current_element_index >= len(current_list):
            current_list_index += 1
            current_element_index = 0
        else:
            yield current_list[current_element_index]
            current_element_index += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
