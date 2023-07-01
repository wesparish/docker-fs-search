import logging
import os
import sys

logging.basicConfig(
  stream=sys.stdout,
  level=getattr(logging, os.getenv('LOG_LEVEL', 'DEBUG')))

class FSLib:
  def __init__(self, data_dir):
    self._data_dir = data_dir

  def normalize_filename(self, filepath):
    logging.debug("FSLib.normalize_filename() called")
    # Strip leading path if it exists
    retval = os.path.basename(filepath)
    # Lowercase for case-insensitive comparison
    retval = retval.lower()
    return retval

  def search_file(self, filename):
    logging.debug("FSLib.search_file() called")
    for root, dirs, files in os.walk(self._data_dir):
      for file in files:
        if file.lower() == filename:
          return True