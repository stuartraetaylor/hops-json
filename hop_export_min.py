#!/usr/bin/env python3

from hop_export import *

fields = [
    'Name',
    'AlphaMax',
    'AlphaMin',
    'BetaMax',
    'BetaMin',
]

export('submodules/sboulema-brewdb/brewDB.sqlite', 'hops-min.json', fields)
