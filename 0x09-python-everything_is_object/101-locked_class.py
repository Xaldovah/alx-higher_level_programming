#!/usr/bin/python3


class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(attr)
                    )
        super().__setattr__(attr, value)
