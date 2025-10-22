# coding: utf-8


##     Copyright (C) 2009-2012 Assem Chelli <assem.ch [at] gmail.com>

##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU Affero General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.

##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU Affero General Public License for more details.

##     You should have received a copy of the GNU Affero General Public License
##     along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ruff: noqa: F601

# Buckwalter Romanization  letters mapping
BUCKWALTER2UNICODE = {
    "'": "\u0621",  # hamza-on-the-line
    "|": "\u0622",  # madda
    ">": "\u0623",  # hamza-on-'alif
    "&": "\u0624",  # hamza-on-waaw
    "<": "\u0625",  # hamza-under-'alif
    "}": "\u0626",  # hamza-on-yaa'
    "A": "\u0627",  # bare 'alif
    "b": "\u0628",  # baa'
    "p": "\u0629",  # taa' marbuuTa
    "t": "\u062a",  # taa'
    "v": "\u062b",  # thaa'
    "j": "\u062c",  # jiim
    "H": "\u062d",  # Haa'
    "x": "\u062e",  # khaa'
    "d": "\u062f",  # daal
    "*": "\u0630",  # dhaal
    "r": "\u0631",  # raa'
    "z": "\u0632",  # zaay
    "s": "\u0633",  # siin
    "$": "\u0634",  # shiin
    "S": "\u0635",  # Saad
    "D": "\u0636",  # Daad
    "T": "\u0637",  # Taa'
    "Z": "\u0638",  # Zaa' (DHaa')
    "E": "\u0639",  # cayn
    "g": "\u063a",  # ghayn
    "_": "\u0640",  # taTwiil
    "f": "\u0641",  # faa'
    "q": "\u0642",  # qaaf
    "k": "\u0643",  # kaaf
    "l": "\u0644",  # laam
    "m": "\u0645",  # miim
    "n": "\u0646",  # nuun
    "h": "\u0647",  # haa'
    "w": "\u0648",  # waaw
    "Y": "\u0649",  # 'alif maqSuura
    "y": "\u064a",  # yaa'
    "F": "\u064b",  # fatHatayn
    "N": "\u064c",  # Dammatayn
    "K": "\u064d",  # kasratayn
    "a": "\u064e",  # fatHa
    "u": "\u064f",  # Damma
    "i": "\u0650",  # kasra
    "~": "\u0651",  # shaddah
    "o": "\u0652",  # sukuun
    "`": "\u0670",  # dagger 'alif
    "{": "\u0671",  # waSla
    # extended here
    "^": "\u0653",  # Maddah
    "#": "\u0654",  # HamzaAbove
    ":": "\u06dc",  # SmallHighSeen
    "@": "\u06df",  # SmallHighRoundedZero
    '"': "\u06e0",  # SmallHighUprightRectangularZero
    "[": "\u06e2",  # SmallHighMeemIsolatedForm
    ";": "\u06e3",  # SmallLowSeen
    ",": "\u06e5",  # SmallWaw
    ".": "\u06e6",  # SmallYa
    "!": "\u06e8",  # SmallHighNoon
    "-": "\u06ea",  # EmptyCentreLowStop
    "+": "\u06eb",  # EmptyCentreHighStop
    "%": "\u06ec",  # RoundedHighStopWithFilledCentre
    "]": "\u06ed",  #
}

# ISO233-2 romanization letter mapping
ISO2UNICODE = {
    "ˌ": "\u0621",  # hamza-on-the-line
    # u"|": u"\u0622", # madda
    "ˈ": "\u0623",  # hamza-on-'alif
    "ˈ": "\u0624",  # hamza-on-waaw
    # u"<": u"\u0625", # hamza-under-'alif
    "ˈ": "\u0626",  # hamza-on-yaa'
    "ʾ": "\u0627",  # bare 'alif
    "b": "\u0628",  # baa'
    "ẗ": "\u0629",  # taa' marbuuTa
    "t": "\u062a",  # taa'
    "ṯ": "\u062b",  # thaa'
    "ǧ": "\u062c",  # jiim
    "ḥ": "\u062d",  # Haa'
    "ẖ": "\u062e",  # khaa'
    "d": "\u062f",  # daal
    "ḏ": "\u0630",  # dhaal
    "r": "\u0631",  # raa'
    "z": "\u0632",  # zaay
    "s": "\u0633",  # siin
    "š": "\u0634",  # shiin
    "ṣ": "\u0635",  # Saad
    "ḍ": "\u0636",  # Daad
    "ṭ": "\u0637",  # Taa'
    "ẓ": "\u0638",  # Zaa' (DHaa')
    "ʿ": "\u0639",  # cayn
    "ġ": "\u063a",  # ghayn
    # u"_": u"\u0640", # taTwiil
    "f": "\u0641",  # faa'
    "q": "\u0642",  # qaaf
    "k": "\u0643",  # kaaf
    "l": "\u0644",  # laam
    "m": "\u0645",  # miim
    "n": "\u0646",  # nuun
    "h": "\u0647",  # haa'
    "w": "\u0648",  # waaw
    "ỳ": "\u0649",  # 'alif maqSuura
    "y": "\u064a",  # yaa'
    "á": "\u064b",  # fatHatayn
    "ú": "\u064c",  # Dammatayn
    "í": "\u064d",  # kasratayn
    "a": "\u064e",  # fatHa
    "u": "\u064f",  # Damma
    "i": "\u0650",  # kasra
    # u"~": u"\u0651", # shaddah
    "°": "\u0652",  # sukuun
    # u"`": u"\u0670", # dagger 'alif
    # u"{": u"\u0671", # waSla
    ##extended here
    # u"^": u"\u0653", # Maddah
    # u"#": u"\u0654", # HamzaAbove
    # u":"  : "\u06DC", # SmallHighSeen
    # u"@"  : "\u06DF", # SmallHighRoundedZero
    # u"\"" : "\u06E0", # SmallHighUprightRectangularZero
    # u"["  : "\u06E2", # SmallHighMeemIsolatedForm
    # u";"  : "\u06E3", # SmallLowSeen
    # u","  : "\u06E5", # SmallWaw
    # u"."  : "\u06E6", # SmallYa
    # u"!"  : "\u06E8", # SmallHighNoon
    # u"-"  : "\u06EA", # EmptyCentreLowStop
    # u"+"  : "\u06EB", # EmptyCentreHighStop
    # u"%"  : "\u06EC", # RoundedHighStopWithFilledCentre
    # u"]"  : "\u06ED"          #
}

# Available romanization systems
ROMANIZATION_SYSTEMS_MAPPINGS = {
    "buckwalter": BUCKWALTER2UNICODE,
    "iso": ISO2UNICODE,
    "arabtex": None,
}


def guess_romanization_system():
    """@todo"""
    pass


def transliterate(mode, string, ignore="", reverse=False):
    """encode & decode different  romanization systems"""

    if ROMANIZATION_SYSTEMS_MAPPINGS.has_key(mode):
        MAPPING = ROMANIZATION_SYSTEMS_MAPPINGS[mode]
    else:
        MAPPING = {}

    if reverse:
        mapping = {}
        for k, v in MAPPING.items():
            # reverse the mapping buckwalter <-> unicode
            mapping[v] = k
    else:
        mapping = MAPPING

    result = ""
    for char in string:
        if mapping.has_key(char) and char not in ignore:
            result += mapping[char]  # test
        else:
            result += char
    return result
