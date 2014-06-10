# -*- coding: utf-8 -*-
import io
dictionary = {}
maps = [u'ę', u'ó', u'ą', u'ś', u'ł', u'ż', u'ź', u'ć', u'ń']


def transform(word):
    encoded_word = u""
    for c in word:
        if c in maps:
            encoded_word = encoded_word + u'ďż˝'
        else:
            encoded_word = encoded_word + c
    return encoded_word

# TODO: zdania
# def enter_text():
#     string = u""
#     text = raw_input('Enter text: ')
#     text = text.decode('utf-8')
#     text = text.split()
#     print text
#     for place, word in enumerate(text):
#         if u'ďż˝' in word:
#             good_word = answer(word)
#             text[place] = good_word
#         else:
#             pass
#     string = u' '.join(str(e) for e in text)
#     print string

# pojedyncze slowo
def question():

    while True:
        malformed = raw_input('Enter malformed word: ')
        malformed = malformed.decode('utf-8')
        answer(malformed)


def answer(malformed):
    if malformed in dictionary:
        for word in dictionary[malformed]:
            print word
    else:
        print "{} dosen't match any of words.".format(malformed)
        print "\n"


def main():
    print "Opening the file..."
    with io.open("dictionary.txt", "rt", encoding="utf-8") as scrabble_file:


        print "Parsing words..."
        for word in scrabble_file:
            word = word.replace(u'\n', u'')

            word = word.replace(u',', u'')
            encoded_word = transform(word.lower())
            dictionary.setdefault((encoded_word), []).append(word)
        print "Finished"
        # pojedyncze slowo
        question()

        # TODO: zdania
        # enter_text()
                # encoded_word = u"".join(mapping[c] for c in word)



if __name__ == "__main__":
    main()
