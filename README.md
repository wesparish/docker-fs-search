# docker-fs-search
This repo provides a simple web UI to search a sub-directory for a specific
filename.

For example, this is useful for a user to ensure that a file was successfully
uploaded to a server.

### Usage
```
Usage: fs-search.py [options]

Options:
  -h, --help            show this help message and exit
  -d DATA_DIR, --data-dir=DATA_DIR
                        data directory to search in
  --debug               Debug mode
  -s, --server          Run web server
```