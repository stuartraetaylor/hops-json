#!/usr/bin/env python3

import sqlite3
import json

def export(db_path, out_path, fields=[]):
    print('Reading database:', db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.execute('select * from Hop order by Id;')
    rs = cursor.fetchall()


    hop_list = []
    for row in rs:
        hop_tuple = {}
        hop_list.append(hop_tuple)

        if not fields:
            fields = row.keys()

        for key in fields:
            hop_tuple[key] = row[key]

    conn.close()

    print('Writing file:', out_path)
    with open(out_path, 'w') as out_file:
        json.dump(hop_list, out_file, indent=2, separators=(',', ': '))

    print('Hops written:', len(hop_list))

