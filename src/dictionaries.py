"""
Helper Module:
Module with dictionaries used throughout project.
"""

suits = {'Clubs'   : '♣',
         'Diamonds': '♦',
         'Hearts'  : '♥',
         'Spades'  : '♠'}

ranks_short_to_long = {'A':  'Ace',
                       '2':  'Two',
                       '3':  'Three',
                       '4':  'Four',
                       '5':  'Five',
                       '6':  'Six',
                       '7':  'Seven',
                       '8':  'Eight',
                       '9':  'Nine',
                       '10': 'Ten',
                       'J':  'Jack',
                       'Q':  'Queen',
                       'K':  'King'}

ranks_long_to_short = {'Ace':   'A',
                       'Two':   '2',
                       'Three': '3',
                       'Four':  '4',
                       'Five':  '5',
                       'Six':   '6',
                       'Seven': '7',
                       'Eight': '8',
                       'Nine':  '9',
                       'Ten':   '10',
                       'Jack':  'J',
                       'Queen': 'Q',
                       'King':  'K'}

short_to_value = {'A':  14,
                  '2':  2,
                  '3':  3,
                  '4':  4,
                  '5':  5,
                  '6':  6,
                  '7':  7,
                  '8':  8,
                  '9':  9,
                  '10': 10,
                  'J':  11,
                  'Q':  12,
                  'K':  13}

suit_to_value = {'Clubs'   : 0,
                 'Diamonds': 1,
                 'Hearts'  : 2,
                 'Spades'  : 3}