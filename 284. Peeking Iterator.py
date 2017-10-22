# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.peekV = self.iter.next() if self.iter.hasNext() else None
        

    def peek(self):
        return self.peekV
        

    def next(self):
        returnVal = self.peekV
        self.peekV = self.iter.next() if self.iter.hasNext() else None
        return returnVal

    def hasNext(self):
        return self.peekV is not None
    