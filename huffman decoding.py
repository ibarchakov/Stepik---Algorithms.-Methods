"""Restore the string from its code and a prefix-free symbols code.
In a first line of the input file there are given two integers k and l in a space —
amount of unique letters in a string and length of encoded string.
In a next k lines there are letters codes in a "letter: code" format. no one code is a prefix of another.
Letters may be shown in any order. All letters are lowercase letters of a Latin alphabet
and each of these letters can be found at least once in a string.
At last in a last line there is an encoded string. The input string and letters codes are not empty.
The input code allows to have the minimum length of the encoded string.
In a first output line show the decoded string s. It should consist of a lowercase letters of a LAtin alphabet.
It is guaranteed that the length of the right answer does not exceed 10**4 symbols.

Sample Input 1:
1 1
a: 0
0

Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

Sample Output 2:
abacabad

"""


def main():
    answer = []
    chars_num, code_length = map(int, input().split())
    code_table = {}
    for _ in range(chars_num):
        a, b = map(str, input().split(':'))
        b = b.strip()
        code_table[b] = a
    coded = str(input())
    start = 0
    end = 1
    while end != len(coded) + 1:
        if coded[start : end] in code_table.keys():
            a = coded[start : end]
            answer.append(code_table[a])
            start = end
            end += 1
        else:
            end += 1
    for _ in answer:
        print(_, end='')



if __name__ == '__main__':
    main()