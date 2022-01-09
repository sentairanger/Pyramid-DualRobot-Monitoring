FROM python:3.8-slim
LABEL maintainer="Edgardo Peregrino"

COPY . /app
WORKDIR /app
# install required modules
RUN pip install -r requirements.txt
# install modules that are found in the setup file
RUN pip install -e .
RUN pip install -e ".[dev]"

# command to run on container start
CMD [ "pserve", "development.ini", "--reload"]
