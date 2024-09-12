
FROM python:3.10-alpine
LABEL authors="doruk.kazanc"

# outputu anlık görmek için.
ENV PYTONUNBUFFERED=1

WORKDIR /djangoProject
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

ENTRYPOINT ["/djangoProject/entrypoint.sh"]