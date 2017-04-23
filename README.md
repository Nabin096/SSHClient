# SSHClient
python app to ssh into a server
fill ine the username and password for ssh connection in app.py
The container should be built first. Command:-
docker build -t testssh .

(PS dont forget the dot at last)
This will install all the requirements and create and image to run.
To run type:
docker run -p <server_port>testssh
this will initiate a ssh connection with the given username and password  into the server


for using a public key app.py should be modified as
after password type: pkey_file = '/home/foo/.ssh/id_rsa'
and in main section: key = paramiko.RSAKey.from_private_key_file(pkey_file)
