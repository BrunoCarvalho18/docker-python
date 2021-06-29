#!usr/bin/env python3
import docker

docker_connection = docker.DockerClient("tcp://172.17.0.1:2376")

#container = docker_connection.containers.run(
#    'debian', 'bin/bash',
#    name='learn', detach=True, tty=True
#)

learn_container = docker_connection.containers.get("learn")
learn_container.start()

#for container in docker_connection.containers.list(all=True):  
#   print(container)

print(docker_connection)