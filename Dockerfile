FROM pypy:3.9-bullseye

RUN pip install -r requirements.txt
COPY . /opt/jobaggrv/

ENTRYPOINT ['python','-m','scrapy']
