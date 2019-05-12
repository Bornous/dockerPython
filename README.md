# dockerPython

To launch there need to be created a user-made docker network

$docker network create -d bridge --subnet 10.10.0.0/24 my_bridge

$docker run --rm -d --net=my_bridge -p 8000:8000 --ip 10.10.0.254 --name my_doc_pyt bornous/dockerpython:latest
