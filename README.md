# dockerPython

To launch there need to be created a user-made docker network

$docker network create -d bridge --subnet 10.10.0.0/24 my_bridge

$docker run --rm -d --net=my_bridge -p 8000:8000 --ip 10.10.0.254 --name my_doc_pyt bornous/dockerpython:latest

If VM machine has address 192.168.56.1 then after configuration shown below u can connect to your docker container via 192.168.56.1:8000 from an outside of VM machine.

   1. Open Oracle VM VirtualBox Manager
   2. Select the VM used by Docker
   3. Click Settings -> Network
   4. Adapter 1 should (default?) be "Attached to: NAT"
   5. Click Advanced -> Port Forwarding
   6. Add rule: Protocol TCP, Host Port 8000, Guest Port 8000 (leave Host IP and Guest IP empty)
   7. Guest is your docker container and Host is your machine
