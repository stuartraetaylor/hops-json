# Hops JSON

A hop database in JSON format - [hops.json](hops.json).

Based on the hop database from [Samir Boulema](https://github.com/sboulema/Hops).

## Usage

1. Clone the repository and submodules.

        git clone --recursive https://github.com/stuartraetaylor/hops-json.git

2. Run the exporter (requires Python 3).

        chmod +x hop-export.py
        ./hop-export.py

The hop database is exported to `hops.json` in the root of the project.

