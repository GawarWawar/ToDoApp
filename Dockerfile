# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables to disable buffer and ensure the correct locale
ENV PYTHONUNBUFFERED=1

RUN python -m venv env
ENV PATH="/env/bin:$PATH"

COPY ./django_instance /django_instance

RUN pip install --upgrade pip && \
    pip install -r /django_instance/requirements.txt

# Set the working directory in the container


# Install any needed packages specified in requirements.txt
RUN ls

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]