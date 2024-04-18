import sys
print('                                      WORD DICTIONARY\n')
words = {'cat':'The cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is commonly referred to as the domestic cat or house cat to distinguish it from the wild members of the family. Wikipedia','dog':"The dog is a domesticated descendant of the wolf. Also called the domestic dog, it is derived from extinct Pleistocene wolves, and the modern wolf is the dog's nearest living relative. Dogs were the first species to be domesticated by hunter-gatherers over 15,000 years ago before the development of agriculture.",'ant':"it is a small animal"}
'dogs'==words['dog']
search=input(' Enter word to search\n')
if search.casefold() == 'cat':
    print(words['cat'])
elif search.casefold() == 'dog':
    print(words['dog'])
elif search.casefold()== 'ant':
    print(words['ant'])
else:
    print('unable to find word')