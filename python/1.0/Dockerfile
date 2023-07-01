FROM python:3

ADD fs-search/requirements.txt /
RUN pip3 install -r requirements.txt

ENV LOG_LEVEL="WARN" LC_ALL=C.UTF-8 LANG=C.UTF-8

WORKDIR /fs-search

ADD fs-search/ /fs-search
# COPY fs-search/fs-search.py /fs-search.py
# RUN chown root:root fs-search.py

EXPOSE 5000

VOLUME "/data"
ENV FS_SEARCH_DATA_DIR="/data"

ENTRYPOINT ["/fs-search/fs-search.py", "--server"]