"""
@url https://www.hackerrank.com/challenges/crossword-puzzle/problem
"""

class Line:

    def __init__(self, start, end, row, crossword, horizontal=True):
        self.start = start
        self.end = end
        self.horizontal = horizontal
        self.crossword = crossword
        self.row = row
        self.base = self.read()

    def __repr__(self):
        return '%s  ({"h" if self.horizontal else "v"} {self.row}, {self.end-self.start} letters)'

    def __len__(self):
        return self.end - self.start

    def __eq__(self, word):

        if len(self) != len(word):
            return False

        for ch1, ch2 in zip(self.read(), word):
            if ch1 != "-" and ch1 != ch2:
                return False
        else:
            return True

    def erase(self):
        self.write(self.base)

    def read(self):
        if self.horizontal:
            row = self.crossword[self.row]
        else:
            row = [self.crossword[i][self.row] for i in range(10)]
        return row[self.start:self.end]

    def write(self, word):
        if self.horizontal:
            old_row = self.crossword[self.row][self.start:self.end]
            self.crossword[self.row][self.start:self.end] = list(word)
        else:
            for letter, i in zip(word, range(self.start, self.end)):
                self.crossword[i][self.row] = letter

    def suitable_words(self, words):
        for word in words:
            if word == self:
                yield word

def find_seq(row):
    seq, not_fullfilled = None, False
    for i, ch in enumerate(row):
        if ch != "+" and ch !="X":
            seq = (i ,i+1) if seq is None else (seq[0], i+ 1)
            if ch == "-":
                not_fullfilled = True
        else:
            if seq is not None and not_fullfilled and seq[1]-seq[0] > 1:
                yield seq
            seq, not_fullfilled = None, False

    if seq is not None and not_fullfilled and seq[1]-seq[0] > 1:
        yield seq

def find_not_filled_line(crossword):
    for i, h_row in enumerate(crossword):
        for seq in find_seq(h_row):
            yield Line(seq[0], seq[1], i, crossword, True)

    for j in range(10):
        v_row = [h_row[j] for h_row in crossword]
        for seq in find_seq(v_row):
            yield Line(seq[0], seq[1], j, crossword, False)

    return None

# Complete the crosswordPuzzle function below.
def solve_crossword(crossword, words):

    try:
        line = next(find_not_filled_line(crossword))
    except StopIteration:
        return crossword

    suitable_words = list(line.suitable_words(words))  # cost = O(n)
    for word in suitable_words:  # cost = O(1), repeats = n

        line.write(word)  # cost = O(1)

        words.remove(word)  # cost = O(1)
        filled_crossword = solve_crossword(crossword, words)  # cost = T(n-1)
        if filled_crossword:
            return filled_crossword
        else:
            words.append(word)
    else:
        line.erase()
        return False

def crosswordPuzzle(crossword, words):
    crossword = [[c for c in line] for line in crossword]
    words = words.split(';')
    result = solve_crossword(crossword, words)
    result = [''.join(row) for row in result]
    return result

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()
    result = crosswordPuzzle(crossword, words)

    print('\n'.join(result))
    print('\n')

