# -*- coding: utf-8 -*-
import io
import re
maps = [u'ę', u'ó', u'ą', u'ś', u'ł', u'ż', u'ź', u'ć', u'ń']
MAGIC_CHAR = u'ď'
words_offset = {}
translated_words = {}


def main():
    print "Opening the dictionary file..."
    with io.open("dictionary.txt", "r", encoding="utf-8") as file:
        scrabble_file = file.read()
    print "Opening the file..."
    with io.open("test.txt", "r", encoding="utf-8") as file:
        data_file = file.read()

    data_file = re.sub(
        re.compile(u'ż˝', re.UNICODE),
        '',
        data_file
    )

    with io.open("test.txt", "w", encoding="utf-8") as file:
        file.write(data_file)

    while True:
        m = re.search(
            re.compile(
                u'\b.+{}.+\b'.format(MAGIC_CHAR),
                re.UNICODE
            ),
            data_file,
        )
        if m is None:
            break
        words_offset.setdefaults(m.group, default=[]).append(m.start)

    print "Finished!"

    print words_offset

    print "Parsing words..."

    for word in words_offset.iterkeys():
        temp = word
        temp.replace(MAGIC_CHAR, u'{}')
        m = re.match(temp.format('|'.join(maps)), scrabble_file)
        translated_words.setdefault(word, default=[]).append(m.groups)
    print "Finished!"

    print "Opening the file..."

    print "Changing know words..."

    for word in words_offset.iterkeys():
        if translated_words[word].len() == 1:
            for offset in words_offset[word]:
                data_file.seek(offset)
                data_file.write(translated_words[word][0])
        else:
            print "Cannot change word - '{}'".format(word)

    with io.open("test.txt", "w", encoding="utf-8") as file:
        file.write(data_file)

    print "Finished!"

if __name__ == "__main__":
    main()
