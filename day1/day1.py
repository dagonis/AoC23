import re

def main():
    data = [_.strip() for _ in open('input.txt', 'r').readlines()]
    # part 1
    print("Part 1:", sum([int(f"{_[0]}{_[-1]}") for _ in [[_ for _ in list(_) if _.isdigit()] for _ in data]])) # Dark Sorcerer Evil Magic
    # part 2
    number_word_re = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    number_words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    print("Part 2:", sum([int(f"{_[0] if _[0].isdigit() else number_words[_[0]]}{_[-1] if _[-1].isdigit() else number_words[_[-1]]}") for _ in [[_ for _ in number_word_re.findall(_)] for _ in data]]))

if __name__ == '__main__':
    main()