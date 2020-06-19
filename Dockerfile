FROM sphinxdoc/sphinx:3.1.1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y rename \
    &&  apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade sphinx_rtd_theme pyyaml

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
RUN make html json \
      && mv _build/json _build/html/json \
      && find _build/html/json -name '*.fjson' | xargs rename "s|.fjson|.json|"

EXPOSE 8888

CMD ["python", "-m", "http.server", "8888", "--directory", "_build/html"]
