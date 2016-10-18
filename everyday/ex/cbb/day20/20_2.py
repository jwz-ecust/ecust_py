import os
from collections import Counter
from nltk.corpus import stopwords


def main():
    for file in os.listdir('.'):
        result = Counter()
        if file.endswith('.txt'):
            with open(file, 'rt') as f:
                for line in f:
                    words = line.split()
                    words = [w for w in words if w not in stopwords.words('eng\
                        lish')]
                    result += Counter(words)
            print "The most important word in %s is %s" %\
                (file, result.most_common(2))


if __name__ == '__main__':
    main()
