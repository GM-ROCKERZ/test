import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com 

321-555-4321
123.555.1234
123-555-1234
800-555-1234
900-555-1234

Mr.Schafer
Mr Snitch
Ms Davis
Mrs. Robinson
Mr .T

'''
sentence = 'Start a sentence and then bring it to the end'

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# pattern = re.compile(r'sentence')
pattern = re.compile(r'start',re.I)
# matches = pattern.finditer(text_to_search)
# matches = pattern.match(sentence)

matches = pattern.search(sentence)
print(matches)
# for match in matches:
# 	print(match)

# with open('data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#      	print(match)



