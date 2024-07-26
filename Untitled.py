# # # Basic list exercises
# # # Fill in the code for the functions below. main() is already set up
# # # to call the functions with a few different inputs,
# # # printing 'OK' when each function is correct.
# # # The starter code for each function includes a 'return'
# # # which is just a placeholder for your code.
# # # It's ok if you do not complete all the functions, and there
# # # are some additional functions to try in list2.py.
# # #Hasna

# # # A. match_ends
# # # Given a list of strings, return the count of the number of
# # # strings where the string length is 2 or more and the first
# # # and last chars of the string are the same.
# # # Note: python does not have a ++ operator, but += works.

# # def match_ends(words):
# #     count=0
# #     for word in words:
# #         length=len(word)
# #         if length>2 and word[0]==word[length-1]:
# #             count+=1
# #     return count


# # # B. front_x
# # # Given a list of strings, return a list with the strings
# # # in sorted order, except group all the strings that begin with 'x' first.
# # # e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# # # ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# # # Hint: this can be done by making 2 lists and sorting each of them
# # # before combining them.

# # def front_x(originalList):
# #     front_x=[]
# #     for word in originalList:
# #         if word[0]=='x':
# #             front_x.append(word)
# #             originalList.remove(word)
# #     sortedList=sorted(originalList)
# #     sortedFrontX=sorted(front_x)
# #     sortedFrontX.extend(sortedList)
# #     print(sortedFrontX)
# #     return


# # # C. sort_last
# # # Given a list of non-empty tuples, return a list sorted in increasing
# # # order by the last element in each tuple.
# # # e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# # # [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# # # Hint: use a custom key= function to extract the last element form each tuple.

# # def sort_last(tuples):
# #     tuple=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# #     def last(tuple):
# #         return tuple[len(tuple)-1]
# #     return(sorted(tuple,key=last))

# # # Simple provided test() function used in main() to print
# # # what each function returns vs. what it's supposed to return.

# # def test(got, expected):
# #     if got == expected:
# #         prefix = ' OK '
# #     else:
# #         prefix = '  X '
# #     print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# # # Calls the above functions with interesting inputs.
# # def main():
# #     print('match_ends')
# #     test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
# #     test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
# #     test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

# #     print()
# #     print('front_x')
# #     test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
# #          ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
# #     test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
# #          ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
# #     test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
# #          ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

# #     print()
# #     print('sort_last')
# #     test(sort_last([(1, 3), (3, 2), (2, 1)]),
# #          [(2, 1), (3, 2), (1, 3)])
# #     test(sort_last([(2, 3), (1, 2), (3, 1)]),
# #          [(3, 1), (1, 2), (2, 3)])
# #     test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
# #          [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
# # if __name__ == "__main__":
# #     main()
# # D. verbing
# # Given a string, if its length is at least 3,
# # add 'ing' to its end.
# # Unless it already ends in 'ing', in which case
# # add 'ly' instead.
# # If the string length is less than 3, leave it unchanged.
# # Return the resulting string.
# # string="hg"
# # if len(string)>2:
# #     if string[-3:]=="ing":
# #         string=string+"ly"
# #     else:
# #         string=string+"ing"
# # print(string)
# # s="This dinner is not that bad!"
# # n=s.find('not')
# # b=s.find('bad')
# # print(s[n:b+3])
# # ss=s.replace(s[n:b+3],"good")
# # print(ss)


# # F. front_back
# # Consider dividing a string into two halves.
# # If the length is even, the front and back halves are the same length.
# # If the length is odd, we'll say that the extra char goes in the front half.
# # e.g. 'abcde', the front half is 'abc', the back half 'de'.
# # Given 2 strings, a and b, return a string of the form
# #  a-front + b-front + a-back + b-back
# # est(front_back('abcd', 'xy'), 'abxcdy')
# #     test(front_back('abcde', 'xyz'), 'abcxydez')
# #     test(front_back('Kitten', 'Donut'), 'KitDontenut')
c='abcd'
b='xy'
def front(a):
    front=""
    point=(len(a)+1)//2
    if len(a)%2==0:
        front=a[:(len(a)//2)]
    else:
        front=a[:point]
    return front
def back(a):
    back=""
    point=(len(a)+1)//2
    if len(a)%2==0:
        back=a[(len(a)//2):]
    else:
        back=a[point:]
    return back
newFront=front(c)+front(b)+back(c)+back(b)
print(newFront)

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# def verbing(s):
#     if len(s)>2:
#         if s[-3:]=="ing":
#             s+="ly"
#         else:
#             s+="ing"
#     return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

# def not_bad(s):
#     findNot=s.find('not')
#     findBad=s.find('bad')
#     if findNot != -1 and findBad != -1 and findBad > findNot:
#         newString=s.replace(s[findNot:findBad+3],"good")
#     return newString


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back


# def front(string):
#         front=""
#         point=(len(string)+1)//2
#         if len(string)%2==0:
#             front=string[:(len(string)//2)]
#         else:
#             front=string[:point]
#             return front
        
# def back(string):
#             back=""
#             point=(len(string)+1)//2
#             if len(string)%2==0:
#                 back=a[(len(a)//2):]
#             else:
#                 back=string[point:]
#             return back
# newFront=front(a)+front(b)+back(a)+back(b)
       


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# def test(got, expected):
#     if got == expected:
#         prefix = ' OK '
#     else:
#         prefix = '  X '
#     print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
# def main():
#     print('verbing')
#     test(verbing('hail'), 'hailing')
#     test(verbing('swiming'), 'swimingly')
#     test(verbing('do'), 'do')

#     print()
#     print('not_bad')
#     test(not_bad('This movie is not so bad'), 'This movie is good')
#     test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
#     test(not_bad('This tea is not hot'), 'This tea is not hot')
#     test(not_bad("It's bad yet not"), "It's bad yet not")

#     print()
#     print('front_back')
#     test(front_back('abcd', 'xy'), 'abxcdy')
#     test(front_back('abcde', 'xyz'), 'abcxydez')
#     test(front_back('Kitten', 'Donut'), 'KitDontenut')


# if __name__ == '__main__':
#     main()
    
    
    
    
