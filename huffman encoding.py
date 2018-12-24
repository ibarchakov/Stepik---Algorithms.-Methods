"""For a given not empty string s of a length not more than 10**4,
consisted of a lowercase letters of a Latin alphabet,
build an optimal prefix-free code. Output the k number of unique letters in a string
and the length of the encoded string in the first line. In the next k lines output the codes of the letters
in a "letter: code" format. In the last line output the encoded string itself.

Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

"""


from collections import Counter, namedtuple
import heapq


class Node (namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf (namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    """The task solved using the Huffman encoding algorithm.
    Huffman tree generates from the exact frequencies of the letters in a text, their weight.
    It goes from the very leaf to the node building new leaves of a sum frequency and weight of its children.
    Then it goes backwards assigning 0 when goes to the left and 1 when goes to the right.
    Thus when reaches the letter we have its prefix-free code.

    """
    h = []
    print(Counter(s))
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    print(h)
    heapq.heapify(h)
    print(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
        print(h)
    code = {}
    if h:
        [(_freq, count, root)] = h
        root.walk(code, '')
    return code


def main():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))
    print(encoded)



if __name__ == '__main__':
    main()
