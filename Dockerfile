FROM python:slim

WORKDIR /app

COPY app.py requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Pull in all the auto instrumentation libs
RUN opentelemetry-bootstrap -a install

EXPOSE 5000
CMD ["opentelemetry-instrument", "python", "app.py"]
