#!/bin/Python
# Decorators
#


def parent(num):

        def first_child():
                return "This is called first_child"
        def second_child():
                return "This is called second_child"

        try:
                assert num == 10
                return first_child
        except AssertionError:
                return second_child

foo = parent(10)
bar = parent(11)

print foo
print bar

print(foo())
print(bar())
