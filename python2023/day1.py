#!/usr/bin/env python3
import time

DIGITS = {"o1e": "one",
          "t2o": "two",
          "t3e": "three",
          "f4r": "four",
          "f5e": "five",
          "s6x": "six",
          "s7n": "seven",
          "e8t": "eight",
          "n9e": "nine"}

DIGITS_DECREASED = dict(reversed(list(DIGITS.items())))



def extractFirstAndLastDigit(line):
    """
    ex : 1abc2 => (1, 2)
         pqr3stu8vwx => (3, 8)
         a1b2c3d4e5f => (1, 5)
         treb7uchet => (7, 7)
    """
    count_digit = 0
    for i in range(len(line)):
        try:
            last_digit_seen = int(line[i])
            if count_digit == 0:
                first_digit = last_digit_seen
                count_digit += 1
            else:
                count_digit += 1
        except ValueError as e:
            continue
    return first_digit, last_digit_seen

def convertWordsToDigit(line):
    """ convert digit words into digit
    """
    for digit, spelling in DIGITS_DECREASED.items():
        line = line.replace(spelling, digit)
    return line

def combineTupleToNumbers(twoDigitsTuple):
    """
    Combine tuple of 2 digits to a two digit decimal number
    ex : (2,4) => 24
    """
    output = twoDigitsTuple[0]*10 + twoDigitsTuple[1]
    return output


def main():
    # with open("../assets/input_day_1.txt", "r") as f:
    with open("../assets/input_example_day_1.txt", "r") as f:
        data = f.readlines()
    t0 = time.time()
    track_sum = 0
    # for line in data[:10]:
    for line in data:
        lineWithDigit = convertWordsToDigit(line)  # FIRST Problem : comment
        print(f"Input : {line.strip()} => {lineWithDigit.strip()}")
        twoDigitTuple = extractFirstAndLastDigit(lineWithDigit)  # FIRST Problem : change lineWithDigit to line
        decimalNumber = combineTupleToNumbers(twoDigitTuple)
        track_sum += decimalNumber
        print(f"First and Last Digit : {twoDigitTuple} => {decimalNumber} (sum = {track_sum})")
    compute_time = time.time()-t0
    print(f"Sum of calibration Value : {track_sum}")

    print(f"Exec time {compute_time}")


if __name__ == "__main__":
    main()
