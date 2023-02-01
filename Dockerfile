FROM python:3.10

#RUN python3 -m venv /opt/venv

# Install dependencies:
COPY config.yml checker.py requirements.txt ./
#RUN . /opt/venv/bin/activate && pip install -r requirements.txt
#RUN . /opt/venv/bin/activate && pip install -r requirements.txt
RUN pip install -r requirements.txt

# Run the application:
# COPY config.yml .
# COPY checker.py .
# CMD . /opt/venv/bin/activate && exec python checker.py
CMD python checker.py