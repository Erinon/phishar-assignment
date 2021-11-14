FROM python:3.9

WORKDIR /app/src

RUN apt update
RUN apt install -y libgl1

COPY src/requirements.txt /app/src/requirements.txt
RUN pip install -r requirements.txt

COPY host_images/ /app/host_images
COPY conf/ /app/conf
COPY src/ /app/src

ENTRYPOINT ["python3"]
CMD ["ris.py"]
