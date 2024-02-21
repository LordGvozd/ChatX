FROM python:3.11

RUN pip3 install poetry
RUN apt update
RUN apt install uvicorn -y

# Download repo
RUN git clone https://github.com/LordGvozd/ChatX.git ./app

# Set workdir
WORKDIR ./app


# Setup poetry
ARG CACHEBUST=1
RUN git pull
RUN poetry install

EXPOSE 80

# Run
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

