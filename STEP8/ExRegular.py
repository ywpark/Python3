# Regular Expressions

import re

# pattern = r'spam' # raw string
#
# if re.match(pattern, 'spamspamspam'): # re.match 는 string beggining 이다
#     print('Match')
# else:
#     print('No match')
#
# if re.match(pattern, 'eggspamsausagespam'):
#     print('Match')
# else:
#     print('No match')
#
# if re.search(pattern, 'eggspamsausagespam'): # re.search 는 pattern anywhere in the string
#     print('search Match')
# else:
#     print('search No match')
#
# print('find all = ', re.findall(pattern, 'eggspamsausagespam')) # re.findall 는 return a list of all substrings that match a pattern


# pattern = r'pam'
#
# match = re.search(pattern, 'eggspamsausage')
# if match:
#     print(match.group()) # returns the string matched
#     print(match.start())
#     print(match.end())
#     print(match.span()) # returns the start and end positions of the first match as a tuple


# str = 'My name is David. Hi David.'
# pattern = r'David'
# newstr = re.sub(pattern, 'Amy', str, 1)
# print(newstr)


# Metacharacters

# pattern = r'gr.y' # dot match any character
#
# if re.match(pattern, 'grey'):
#     print('Match 1')
#
# if re.match(pattern, 'gray'):
#     print('Match 2')
#
# if re.match(pattern, 'blue'):
#     print('Match 3')


# pattern = r'^gr.y$' # ^ : start , $ : end
#
# if re.match(pattern, 'grey'):
#     print('Match')
#
# if re.match(pattern, 'gray'):
#     print('Match')
#
# if re.search(pattern, 'stingray'):
#     print('Match')



# Character Classes

# pattern = r'[aeiou]' # only one of a specific set of characters.
#
# if re.search(pattern, 'grey'):
#     print('Match 1')
#
# if re.search(pattern, 'qwertyiop'):
#     print('Match 2')
#
# if re.search(pattern, 'rhythm myths'):
#     print('Match 3')


# pattern = r'[A-Z][A-Z][0-9]' # match ranges of characters.
#
# if re.search(pattern, 'LS8'):
#     print('Match 1')
#
# if re.search(pattern, 'E3'):
#     print('Match 2')
#
# if re.search(pattern, '1ab'):
#     print('Match 3')

# pattern = r'[^A-Z]' # ^ 반대의 의미 ( invert )
#
# if re.search(pattern, 'this is all quiet.'):
#     print('Match 1')
#
# if re.search(pattern, 'AbCdEfG123'):
#     print('Match 2')
#
# if re.search(pattern, 'THISISALLSHOUTING'):
#     print('Match 3')


# Metacharacters
#
# pattern = r'egg(spam)*' #  * zero or more repetitions of the previous thing
#                         # () * 에서 말한 previous thing can be a single character, a class, or a group of characters in parentheses
#
# if re.match(pattern, 'egg'):
#     print('Match 1')
#
# if re.match(pattern, 'eggspamspamegg'):
#     print('Match 2')
#
# if re.match(pattern, 'spam'):
#     print('Match 3')

# pattern = r'g+' #  + one or more repetitions
#
# if re.match(pattern, 'g'):
#     print('Match 1')
#
# if re.match(pattern, 'ggggggggggggggg'):
#     print('Match 2')
#
# if re.match(pattern, 'gabc'):
#     print('Match 3')


# pattern = r'ice(-)?cream' # ? means zero or one repetitions
#
# if re.match(pattern, 'ice-cream'):
#     print('Match 1')
#
# if re.match(pattern, 'icecream'):
#     print('Match 2')
#
# if re.match(pattern, 'sausages'):
#     print('Match 3')
#
# if re.match(pattern, 'ice--ice'):
#     print('Match 4')

# pattern = r'9{1,3}$' # {x,y} between x and y repetitions of something
#
# if re.match(pattern, '9'):
#     print('Match 1')
#
# if re.match(pattern, '999'):
#     print('Match 2')
#
# if re.match(pattern, '9999'):
#     print('Match 3')


# Groups

# pattern = r'egg(spam)*'
#
# if re.match(pattern, 'egg'):
#     print('Match 1')
#
# if re.match(pattern, 'eggspamspamspamegg'):
#     print('Match 2')
#
# if re.match(pattern, 'spam'):
#     print('Match 3')

# # groups in a match can be accessed
# pattern = r'a(bc)d'
# #pattern = r'[a-z]@([a-z].[a-z])'
#
# match = re.match(pattern, 'abcdefghijklmnop')
# #match = re.match(pattern, 'a@b.d')
#
#
# if match:
#     print(match.group())   # whole match
#     print(match.group(0))  # whole match
#     print(match.group(1))  # nth group from the left
#     #print(match.group(2))
#     print(len(match.groups()))  # all groups


# # group naming 형식 -> (?P<name>...) name 으로 접근가능하다
# # Non-capturing groups -> (?:...) 형식은 group 메소드로 접근이 불가능하다
# pattern = r'(?P<first>abc)(?:def)(ghi)'
#
# match = re.match(pattern, 'abcdefghi')
#
# if match:
#     print(match.group('first'))
#     print(match.groups())


# pattern = r'gr(a|e)y' # | -> or 의 의미 red|blue 'red' or 'blue'
#
# match = re.match(pattern, 'gray')
#
# if match:
#     print('Match 1')
#
# match = re.match(pattern, 'grey')
#
# if match:
#     print('Match 2')
#
# match = re.match(pattern, 'graey')
#
# if match:
#     print('Match 3')

# Special Sequences

# pattern = r'(.+) \0' # \1 means a repetition of what was found in group number 1
#
# match = re.match(pattern, 'word word')
# if match:
#     print('Match 1')
#
# match = re.match(pattern, '?! ?!')
# if match:
#     print('Match 2')
#
# match = re.match(pattern, 'abc cde')
# if match:
#     print('Match 3')

# pattern = r'(\D+\d)' # 대문자는 소문자의 반대 의미
#                      # \d : digits, \s : whitespace , \w : word characters
#
# match = re.match(pattern, 'Hi 999!')
# if match:
#     print('Match 1')
#
# match = re.match(pattern, '1, 23, 456!')
# if match:
#     print('Match 2')
#
# match = re.match(pattern, '!$?233')
# if match:
#     print('Match 3')

# pattern = r'\b(cat)\b' # \A , \Z : match the beginning and end of a string
#                        # \b : 일반적인 character 가 아닌 것들
#
# match = re.search(pattern, 'The cat sat!')
# if match:
#     print('Match 1')
#
# match = re.search(pattern, 'We s>cat<tered?')
# if match:
#     print('Match 2')
#
# match = re.search(pattern, 'We @cat#tered.')
# if match:
#     print('Match 3')


# Email Extraction

pattern = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'
str = 'Please contact in123234-.fo@solo-lean.com for assistance'

match = re.search(pattern, str)
if match:
    print(match.group())