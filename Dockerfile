FROM sphinxdoc/sphinx:8.2.3 AS docsbuilder

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y rename \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#RUN pip3 install --upgrade "Sphinx==8.2.3" "sphinx_rtd_theme>=3,<4" "pyyaml>=6,<7"
RUN pip3 install --upgrade "sphinx_rtd_theme>=3,<4" "pyyaml>=6,<7"

WORKDIR /srv/app

COPY ./ ./

RUN rm -rf _build

ARG PORTAL
RUN make html json \
      && mv _build/json _build/html/json \
      && find _build/html/json -name '*.fjson' | xargs rename "s|.fjson|.json|"

FROM nginx:1.30

RUN rm -rf /usr/share/nginx/html/*

COPY --from=docsbuilder /srv/app/_build/html /usr/share/nginx/html
