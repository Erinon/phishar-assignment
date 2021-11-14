FROM python:3.9

WORKDIR /src

RUN apt update
RUN apt install -y libgl1

COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src

ENTRYPOINT ["python3"]
CMD ["ris.py"]
