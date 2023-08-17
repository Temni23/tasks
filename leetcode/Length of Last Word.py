# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
#  A word is a maximal  substring consisting of non-space characters only.


s = "    Hello World       "


def max_len(s: str) -> int:
    word_list = s.split(' ')
    while True:
        try:
            word_list.remove('')
        except:
            break
    last_el = (word_list.pop())
    result = len(last_el)
    return result


print(max_len(s))
