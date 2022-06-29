FROM python:3.8.13-slim

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /usr/app/entrypoint.sh

#RUN groupadd -g 999 python && \
#    useradd -r -u 999 -g python python
#USER 999

EXPOSE 8000
ENTRYPOINT ["/usr/app/entrypoint.sh"]
