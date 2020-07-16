"""
Attempt to create a burrows-wheeler transform for text only. The text can only contain characters
that are typable on a keyboard. Methods used will include counting sort, suffix array, cyclic rotation,
index mapping, prefix doubling etc..
"""

class BWT():

    def __init__(self, filename):
        # read file
        self.txt = self.file_to_string(filename) + "€" # add termination
        self.suffix_array = []
        self.string_array = []

        # generate suffix array
        for t in range(len(self.txt)):
            self.string_array.append(self.txt[t])
            self.suffix_array.append(t)

        # sort first column of suffix array w/ counting sort
        n = len(self.string_array)
        buckets = [None] * 97
        for i in range(len(buckets)):
            buckets[i] = []
        for i in range(n):
            pos = self.ord2(self.string_array[i])
            buckets[pos].append(self.suffix_array[i])
        temp = []
        for i in range(len(buckets)):
            for j in buckets[i]:
                temp.append(j)
        print(self.string_array)
        print(self.suffix_array)
        self.suffix_array = temp
        del temp # saving space
        for i in self.suffix_array:
            print(self.string_array[i], end="")
        print("")
        print(self.suffix_array)

        # prefix doubling with mergesort
        k = 1

        pass

    def file_to_string(self, filename):
        f = open(filename, "r")
        tx = f.read()
        return tx

    def ord2(self, char):
        '''
        outputs a numeric representation of a character
        € = end of text

        ord readjusted, original smallest was 10, changed '\n' to ord 1 instead
        and made everything else -30 to save space! (10-31 all redundant)
        '''
        if char == '€':
            rank = 0
        elif char == "\n":
            rank = 1
        else:
            rank = ord(char)-30
        assert rank < 97, "invalid character found, check readme!"
        return rank

    def merge_sort(self, arr):
        """
        specialized merge sort for bwt
        """

if __name__ == "__main__":
    # bwt = BWT("texts\sample1.txt")
    # bwt = BWT("texts\everytest.txt")
    bwt = BWT("texts\mississippi.txt")
    pass
