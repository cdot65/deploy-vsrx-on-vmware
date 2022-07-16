FROM python:3.10-alpine

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="deploy-vsrx-on-vmware"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="ansible container to deploy vsrx on VMware"
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/deploy-vsrx-on-vmware"
LABEL build-date="20220713"


# ---------------------------------------------------------------------------
# Change directory to /home/ansible
# ---------------------------------------------------------------------------
WORKDIR /home/ansible

# ---------------------------------------------------------------------------
# Add and install python packages
# ---------------------------------------------------------------------------
ADD docker/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---------------------------------------------------------------------------
# Install Ansible Galaxy roles and collections
# ---------------------------------------------------------------------------
RUN ansible-galaxy collection install juniper.device
RUN ansible-galaxy collection install community.vmware

# ---------------------------------------------------------------------------
# COPY FILES TO CONTAINER IMAGE
# ---------------------------------------------------------------------------
COPY docker/ansible.cfg /etc/ansible/ansible.cfg
COPY ansible/inventory.yaml inventory.yaml
COPY ansible/deploy.vsrx.yaml deploy.vsrx.yaml
COPY ansible/test.yaml test.yaml

### ---------------------------------------------------------------------------
### Environmentals
### ---------------------------------------------------------------------------
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
