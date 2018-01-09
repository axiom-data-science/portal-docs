FROM node:4

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    python2.7-dev \
    python-sphinx \
  && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    apt-get install -y python-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade \
    sphinx_rtd_theme \
    hieroglyph \
    rst2pdf

RUN npm install -g http-server

RUN mkdir -p /srv/app

WORKDIR /srv/app

RUN useradd --system --home-dir=/srv/app app \
      && chown -R app:app /srv/app
USER app

COPY ./ ./

USER root
RUN chown -R app:app /srv/app
USER app

RUN rm -rf _build

ARG PORTAL
RUN make html

EXPOSE 8888

CMD ["http-server", "_build/html", "-p", "8888", "-d", "false"]
