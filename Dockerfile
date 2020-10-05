FROM sphinxdoc/sphinx:3.1.1 as docsbuilder

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y rename \
    &&  apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade sphinx_rtd_theme pyyaml

WORKDIR /srv/app

COPY ./ ./

RUN rm -rf _build

ARG PORTAL
RUN make html json \
      && mv _build/json _build/html/json \
      && find _build/html/json -name '*.fjson' | xargs rename "s|.fjson|.json|"

FROM nginx:1.18

RUN rm -rf /usr/share/nginx/html/*

COPY --from=docsbuilder /srv/app/_build/html /usr/share/nginx/html
