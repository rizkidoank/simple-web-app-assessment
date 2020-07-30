FROM alpine:3.12.0
RUN apk add --no-cache python3 &&\
    ln -sf python3 /usr/bin/python
COPY src/ /app
WORKDIR /app
CMD ["python", "app.py"]