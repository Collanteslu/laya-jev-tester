FROM python:3.12-alpine

WORKDIR /app

RUN addgroup -S laya && adduser -S -G laya laya

COPY index.html server.py favicon.svg favicon-32.png apple-touch-icon.png ./

USER laya

ENV HOST=0.0.0.0 PORT=8899
EXPOSE 8899

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8899/', timeout=2).status==200 else 1)"

CMD ["python", "server.py"]
