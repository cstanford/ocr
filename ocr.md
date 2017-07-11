# Interview Information #

We would like to see some code of yours. In order to do this, we have selected a short programming exercise so that we can see your style and approach to problems. Please spend some time solving the following problem in whatever language and style you like. We hope that this will not take too much time and ask that you not spend more than 3 hours on it, although we do not mean for this to imply that you should spend up to three hours. This is meant to be short and not burdensome in order that we have a sample of your own code for the interview.

We would like for you to put your code online on a free sharing site like Github or Bitbucket.


##Problem Description##

###User Story 1###

You work for a bank, which has recently purchased an ingenious machine
to assist in reading letters and faxes sent in by branch offices. The
machine scans the paper documents, and produces a file with a number of
entries which each look like this:

        _  _     _  _  _  _  _
      | _| _||_||_ |_   ||_||_|
      ||_  _|  | _||_|  ||_| _|


Each entry is 4 lines long, and each line has 27 characters. The first 3
lines of each entry contain an account number written using pipes and
underscores, and the fourth line is blank. Each account number should
have 9 digits, all of which should be in the range 0-9. A normal file
contains around 500 entries.

Your first task is to write a program that can take this file and parse
it into actual account numbers.

###User Story 2###

Having done that, you quickly realize that the ingenious machine is not
in fact infallible. Sometimes it goes wrong in its scanning. The next
step therefore is to validate that the numbers you read are in fact
valid account numbers. A valid account number has a valid checksum. This
can be calculated as follows:

    account number:  3  4  5  8  8  2  8  6  5
    position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1

    checksum calculation:
    (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0

So now you should also write some code that calculates the checksum
for a given number, and identifies if it is a valid account number. Be
very careful to read the definition of checksum correctly. It is not a
simple dot product, the digits are reversed from what you expect.

## Clues##

I recommend finding a way to write out 3x3 cells on 3 lines in your
code, so they form an identifiable digits. Even if your code actually
doesn't represent them like that internally. I'd much rather read

    "   " +
    "|_|" +
    "  |"

than

    "   |_|  |"

anyday.

## Suggested Test Cases ##

If you want to just copy and paste these test cases into your editor, I
suggest first clicking "edit this page" so you can see the source. Then
you can be sure to copy across all the whitespace necessary. Just don't
save any changes by mistake.

    use case 1
     _  _  _  _  _  _  _  _  _
    | || || || || || || || || |
    |_||_||_||_||_||_||_||_||_|

    => 000000000

      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |

    => 111111111
     _  _  _  _  _  _  _  _  _
     _| _| _| _| _| _| _| _| _|
    |_ |_ |_ |_ |_ |_ |_ |_ |_

    => 222222222
     _  _  _  _  _  _  _  _  _
     _| _| _| _| _| _| _| _| _|
     _| _| _| _| _| _| _| _| _|

    => 333333333

    |_||_||_||_||_||_||_||_||_|
      |  |  |  |  |  |  |  |  |

    => 444444444
     _  _  _  _  _  _  _  _  _
    |_ |_ |_ |_ |_ |_ |_ |_ |_
     _| _| _| _| _| _| _| _| _|

    => 555555555
     _  _  _  _  _  _  _  _  _
    |_ |_ |_ |_ |_ |_ |_ |_ |_
    |_||_||_||_||_||_||_||_||_|

    => 666666666
     _  _  _  _  _  _  _  _  _
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |

    => 777777777
     _  _  _  _  _  _  _  _  _
    |_||_||_||_||_||_||_||_||_|
    |_||_||_||_||_||_||_||_||_|

    => 888888888
     _  _  _  _  _  _  _  _  _
    |_||_||_||_||_||_||_||_||_|
     _| _| _| _| _| _| _| _| _|

    => 999999999
        _  _     _  _  _  _  _
      | _| _||_||_ |_   ||_||_|
      ||_  _|  | _||_|  ||_| _|

    => 123456789

     _  _  _  _  _  _  _  _
    | || || || || || || ||_   |
    |_||_||_||_||_||_||_| _|  |

    => 000000051
        _  _  _  _  _  _     _
    |_||_|| || ||_   |  |  | _
      | _||_||_||_|  |  |  | _|

    => 490067715
     _     _  _  _  _  _  _
    | || || || || || || ||_   |
    |_||_||_||_||_||_||_| _|  |

    => 000000051
        _  _  _  _  _  _     _
    |_||_|| ||_||_   |  |  | _
      | _||_||_||_|  |  |  | _|

    => 490867715
