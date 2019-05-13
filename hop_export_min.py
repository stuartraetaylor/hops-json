#!/usr/bin/env python3

from hop_export import *

fields = [
    'Name',
    'AlphaMax',
    'AlphaMin',
    'BetaMax',
    'BetaMin',
]

export('submodules/sboulema-hops/src/Hops/hops.sqlite', 'hops-min.json', fields)
