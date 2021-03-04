FROM python:3

ENV GOSU_VERSION 1.10
RUN curl -sS -Lo /usr/bin/gosu https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64
RUN chmod +x /usr/bin/gosu

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV GIST_URL https://gist.githubusercontent.com/LucasVmigotto/850418a9b47757fb3006cdd9be2c29cb/raw/c1aa16865af0d623a5e1319d65acde0070712ba5/entrypoint-python.sh
RUN curl -sS $GIST_URL > /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

VOLUME /app
WORKDIR /app

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
CMD [ python ]
