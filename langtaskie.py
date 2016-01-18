train_txt = open('train.txt', 'r', encoding='utf-8')
test_txt = open('test.txt', 'r', encoding='utf-8')
output_txt = open('output.txt', 'w', encoding='utf-8')

myDict = {}


def create_dictionary(txt):
    for line in txt:
        lang, *text = line.strip().split()

        if lang not in myDict:
            myDict[lang] = {}

        for word in text:
            if word not in myDict[lang]:
                myDict[lang][word] = 1


def line_classifier(txt):
    score = dict.fromkeys(myDict.keys(), 0)

    for word in txt.split():
        for lang in myDict:
            if word in myDict[lang]:
                score[lang] += 1

    s = 0
    for lang in score:
        if score[lang] > s:
            s = score[lang]
            res = lang

    if s < 2:
        for word in txt.split():
            for lang in myDict:
                if word in myDict[lang]:
                    score[lang] +=1
                elif len(word)>2:
                    for dict_word in myDict[lang]:
                        if len(dict_word) > 2:
                            if dict_word in word or word in dict_word:
                                score[lang] +=1
        s = 0
        for lang in score:
            if score[lang] > s:
                s = score[lang]
                res = lang
        return res

    return res


def language_classifier():
    for line in test_txt:
        line = line.strip()
        lang = line_classifier(line)
        output_txt.write(lang + '\n')


create_dictionary(train_txt)
language_classifier()
train_txt.close()
test_txt.close()
output_txt.close()
