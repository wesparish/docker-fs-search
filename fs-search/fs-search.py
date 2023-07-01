#!/usr/bin/env python3
'''
Used to search for a specific file in a specific sub-path
Provides a simple Flask web UI
'''

from optparse import OptionParser

import datetime
import logging
import os
import sys
import time

from flask import Flask, render_template, request
from prometheus_client import Counter, Summary, generate_latest

from lib.fs import FSLib

logging.basicConfig(
  stream=sys.stdout,
  level=getattr(logging, os.getenv('LOG_LEVEL', 'DEBUG')))

parser = OptionParser()
parser.add_option("-d",
                  "--data-dir",
                  default=os.getenv("FS_SEARCH_DATA_DIR", "."),
                  help="data directory to search in")
parser.add_option("--debug",
                  dest="debug",
                  default=False,
                  help="Debug mode", action="store_true")
parser.add_option("-s", "--server", dest="server", default=False,
                  help="Run web server", action="store_true")
(options, args) = parser.parse_args()

print("options: %s" % options)

app = Flask(__name__)
fs_lib = FSLib(options.data_dir)

search_total = Counter(
  'search_total',
  'Total file searches')
search_duration = Summary(
  'search_duration_ms',
  'Time spent searching for files')

# @search_duration.time()
# @search_total.inc()
@app.route('/search', methods=['post'])
def search_file():
    filepath = request.form['filepath']
    result_str = "Looking for file: [%s]... " % (filepath)
    if fs_lib.search_file(fs_lib.normalize_filename(filepath)):
      result_str = "%s%s%s" % (
         '&check;&check;&check;',
         result_str,
         'found &check;&check;&check;')
    else:
      result_str = "%s%s%s" % (
         '&cross;&cross;&cross;',
         result_str,
         'NOT found &cross;&cross;&cross;')
    return result_str

@app.route('/', methods=['get'])
def search_page():
    return render_template(
        'search.html',
        options=options)

@app.route('/metrics')
def metrics():
    return generate_latest()

if options.server:
  app.run(debug=options.debug, host='0.0.0.0')