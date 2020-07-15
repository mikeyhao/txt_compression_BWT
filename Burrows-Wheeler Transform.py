"""
Attempt to create a burrows-wheeler transform for text only. The text can only contain characters
that are typable on a keyboard. Methods used will include counting sort, suffix array, cyclic rotation,
index mapping, prefix doubling etc..
"""

class BWT():

    def __init__(self, filename):
        # read file
        self.txt = self.file_to_string(filename)
        self.txt += "€"    # add termination
        for t in self.txt:
            pass
        pass

    def file_to_string(self, filename):
        f = open(filename, "r")
        tx = f.read()
        return tx

    def ord2(self, char):
        '''
        outputs a numeric representation of a character
        € = end of text
        £ = new line
        0 = represents
        '''
        pass

if __name__ == "__main__":
    bwt = BWT("texts\sample1.txt")
    pass
