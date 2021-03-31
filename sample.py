import re

text_to_search = """
http://cprey.com
https://www.google.com
https://www.nasa.gov

Mr. Saou
Mr Right
Ms. Dao
Mrs. T
"""
sentence = "Start with sth and bring it to the end."

pattern_1 = re.compile(r'(Mr|Mrs|Ms)\.?')
pattern_2 = re.compile(r'(w{3}.)?(\w+)(\.\w+)')
pattern_3 = re.compile(r'start', re.IGNORECASE) # make case unsensitive
pattern_4 = re.compile(r'with')

matches_1 = pattern_1.finditer(text_to_search)
matches_2 = pattern_2.findall(text_to_search)
matches_3 = pattern_3.match(sentence)
# match only works for chars at the beginning, not in the middle
# search works for chars in the middle
matches_4 = pattern_4.search(sentence)

for match in matches_1:
    print(match)

for match in matches_2:
    print(match)

print(matches_3)

print(matches_4)
