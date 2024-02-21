FROM python:3.11

# Download repo
RUN git clone https://github.com/LordGvozd/ChatX.git ./app

# Set workdir
WORKDIR ./app

RUN ls -a >> /tmp/lagalaga
# Setup poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip3 install poetry
RUN cat /tmp/lagalaga && poetry install
RUN poetry shell

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

