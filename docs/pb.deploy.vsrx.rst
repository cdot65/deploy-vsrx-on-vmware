===================
pb.deploy.vsrx.yaml
===================

-------------------------------------------
deploy a virtual firewall on VMware vCenter
-------------------------------------------

deploy.vsrx
===========

This module will deploy a vSRX on VMware vCenter

Example
-------

Here is a basic example of using the module to deploy a vSRX.

You'll need to pass in some parameters, as shown below

.. code-block:: yaml

    ---
    ### ---------------------------------------------------------------------------
    ### DEPLOY vSRX
    ### ---------------------------------------------------------------------------
    - hosts: "localhost"
      connection: local
      gather_facts: False
      become: False
      tasks:

        - name: "### CLONE A VSRX ###"
          community.vmware.vmware_guest:
            hostname: "{{ vcenter_hostname }}"
            username: "{{ vcenter_username }}"
            password: "{{ vcenter_password }}"
            datacenter: "{{ datacenter }}"
            state: present
            folder: "{{ folder }}"
            template: "{{ template }}"
            name: "{{ vm_name }}"
            esxi_hostname: "{{ esxi_host }}"
            wait_for_ip_address: True
            validate_certs: False
          delegate_to: localhost
          register: vsrx_details
