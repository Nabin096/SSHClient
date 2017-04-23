FROM python:2.7
FROM Ubuntu:16.04

WORKDIR /app
# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get -y install gcc python python-pip
RUN pip install -r requirements.txt

EXPOSE 80
ENV NAME Sshtest
# Run app.py when the container launches
CMD ["python", "app.py"]
