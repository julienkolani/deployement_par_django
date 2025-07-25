
FROM python:3.9.18-slim-bullseye

RUN mkdir -p /home/app/test_app

COPY test_app /home/app/test_app

# Installation des outils nécessaires

RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked     --mount=type=cache,target=/var/lib/apt,sharing=locked     --mount=type=cache,target=/root/.cache     apt-get update -y; \  
    apt-get update --no-cache-dir -y;     apt-get -o APT::Install-Recommends=false upgrade;     mkdir -p /home/app/test_app/static;     pip install --upgrade pip &&     pip install -r /home/app/test_app/requirements.txt &&     pip install uvicorn &&     python3 /home/app/test_app/manage.py collectstatic --noinput
    
RUN apt-get remove --purge pip ;     apt-get autoremove

EXPOSE 8000

CMD ["bash", "-c", "cd /home/app/test_app && uvicorn test_app.asgi:application --host 0.0.0.0 --port 8000"]
