"""
This module defines the sorting order and comparator function
for sorting according to the sorting order of Bangla Academy.

Map / Dictionary-based Algorithm initially proposed by:
Shabnam, Aamira, Tapashee Tabassum Urmi, and Md Saiful Islam.
"A Faster Approach to Sort Unicode Represented Bengali Words."
International Journal of Computer Applications 126.11 (2015).

Usage:
from bangla_sort import bangla

sorted(list, key=bangla)
"""

char_map = {
    "\u0985": 0,
    "\u0986": 1,
    "\u0987": 2,
    "\u0988": 3,
    "\u0989": 4,
    "\u098A": 5,
    "\u098B": 6,
    "\u098F": 7,
    "\u0990": 8,
    "\u0993": 9,
    "\u0994": 10,
    "\u0995": 11,
    "\u0996": 12,
    "\u0997": 13,
    "\u0998": 14,
    "\u0999": 15,
    "\u099A": 16,
    "\u099B": 17,
    "\u099C": 18,
    "\u099D": 19,
    "\u099E": 20,
    "\u099F": 21,
    "\u09A0": 22,
    "\u09A1": 23,
    "\u09A2": 24,
    "\u09A3": 25,
    "\u09A4": 26,
    "\u09A5": 27,
    "\u09A6": 28,
    "\u09A7": 29,
    "\u09A8": 30,
    "\u09AA": 31,
    "\u09AB": 32,
    "\u09AC": 33,
    "\u09AD": 34,
    "\u09AE": 35,
    "\u09AF": 36,
    "\u09B0": 37,
    "\u09B2": 38,
    "\u09B6": 39,
    "\u09B7": 40,
    "\u09B8": 41,
    "\u09B9": 42,
    "\u09DC": 43,
    "\u09DD": 44,
    "\u09DF": 45,
    "\u09CE": 46,
    "\u0982": 47,
    "\u0983": 48,
    "\u0981": 49,
    "\u09BE": 50,
    "\u09BF": 51,
    "\u09C0": 52,
    "\u09C1": 53,
    "\u09C2": 54,
    "\u09C3": 55,
    "\u09C7": 56,
    "\u09C8": 57,
    "\u09CB": 58,
    "\u09CC": 59,
    "\u09CD": 60,
    "\u09BC": 61,
    "\u09D7": 62
}


def bangla(item: str):
    return [char_map.get(x, ord(x)) for x in item]
