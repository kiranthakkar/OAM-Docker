resource "null_resource" "remote-exec" {
    depends_on = ["oci_core_instance.OAMTFInstance"]
     provisioner "file" {
        connection {
                user = "opc"
                type = "ssh"
                host = "${data.oci_core_vnic.InstanceVnic.public_ip_address}"
                private_key = "${var.ssh_private_key}"
                agent = false
        }
        source = "userdata/oamscript"
        destination = "/home/opc"
  }

  provisioner "remote-exec" {
        connection {
                user = "opc"
                type = "ssh"
                host = "${data.oci_core_vnic.InstanceVnic.public_ip_address}"
                agent = false
                private_key = "${var.ssh_private_key}"
        }
        inline = [
         "chmod +x /home/opc/oamscript/*.sh",
	 "cd /home/opc/oamscript",
         "./build.sh"
        ]
  }
}
