# FROM python:3.11.1-slim-bullseye

# ENV PYTHONUNBUFFERED 1
# WORKDIR /build

# # Create venv, add it to path and install requirements
# RUN python -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# COPY requirements.txt .
# RUN pip install --upgrade pip setuptools wheel
# RUN pip install -r requirements.txt

# # Install uvicorn server
# RUN pip install uvicorn[standard]

# # Copy the rest of app
# COPY app app
# COPY alembic alembic
# COPY alembic.ini .
# COPY pyproject.toml .
# COPY init.sh .

# # Print "ready" when the container is ready
# RUN echo "ready"
# EXPOSE 8000
# EXPOSE 80