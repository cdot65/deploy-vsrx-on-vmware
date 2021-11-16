"""Tasks for use with Invoke.

(c) 2021 Calvin Remsburg
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from invoke import task

### ---------------------------------------------------------------------------
### DOCKER PARAMETERS
### ---------------------------------------------------------------------------
DOCKER_IMG = "registry.gitlab.com/cremsburg/juniper-automation-container"
DOCKER_TAG = "deploy-vsrx"

### ---------------------------------------------------------------------------
### SYSTEM PARAMETERS
### ---------------------------------------------------------------------------
PWD = os.getcwd()

### ---------------------------------------------------------------------------
### VCENTER PARAMETERS
### ---------------------------------------------------------------------------
VCENTER_HOSTNAME='vcenter.dmz.home'
VCENTER_USERNAME='ansible@dmz.home'
VCENTER_PASSWORD='ansible123'
DATACENTER='home'
FOLDER='/NetworkVirtualization'
TEMPLATE='vsrx3_21.x'
ESXI_HOST='esx5.dmz.home'
VM_NAME='ansible-test'

### ---------------------------------------------------------------------------
### DOCKER CONTAINER BUILD
### ---------------------------------------------------------------------------
@task
def container(context):
    # Build our docker image
    context.run(
        f"docker build -t {DOCKER_IMG}:{DOCKER_TAG} files/docker/",
    )

### ---------------------------------------------------------------------------
### DOCKER CONTAINER SHELL
### ---------------------------------------------------------------------------
@task
def shell(context):
    # Get access to the BASH shell within our container
    print("Jumping into container, type exit to return to host")
    context.run(
        f"docker run -it --rm \
            -v {PWD}/files/:/home/tmp/files \
            -v {PWD}/files/:/home/tmp/files \
            -w /home/tmp/files/ansible/ \
            {DOCKER_IMG}:{DOCKER_TAG} /bin/bash",
        pty=True,
    )


### ---------------------------------------------------------------------------
### EXECUTE PLAYBOOK FROM WITHIN CONTAINER
### ---------------------------------------------------------------------------
@task
def ansible(context):
    # Execute Ansible playbook from within the container
    context.run(
        f"docker run -it \
            --rm \
            -v {PWD}/files/ansible/:/home/ansible \
            -w /home/ansible/ \
            {DOCKER_IMG}:{DOCKER_TAG} ansible-playbook -vvv pb.deploy.vsrx.yaml \
            -e vcenter_hostname='{VCENTER_HOSTNAME}' \
            -e vcenter_username='{VCENTER_USERNAME}' \
            -e vcenter_password='{VCENTER_PASSWORD}' \
            -e datacenter='{DATACENTER}' \
            -e folder='{FOLDER}' \
            -e template='{TEMPLATE}' \
            -e esxi_host='{ESXI_HOST}' \
            -e vm_name='{VM_NAME}'",
        pty=True,
    )
