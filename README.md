# Hops JSON

A hop database in JSON format - [hops.json](hops.json).

Based on the [BrewDB database](https://github.com/sboulema/BrewDB)
from [Samir Boulema](https://github.com/sboulema).

## Usage

1. Clone the repository and submodules.

        git clone --recursive https://github.com/stuartraetaylor/hops-json.git

2. Run the exporter (requires Python 3).

        chmod +x hop_export_full.py
        ./hop_export_full.py

The hop database is exported to `hops.json` in the root of the project.

