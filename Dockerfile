FROM python:3.11

# Download repo
RUN git clone https://github.com/LordGvozd/ChatX.git ./app

cd ./app

# Setup poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install
RUN poetry shell

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

