resource "oci_core_instance" "OAMTFInstance" {
  # depends_on = ["oci_database_db_system.IDMDBNode"]
  availability_domain = "${lookup(data.oci_identity_availability_domains.ADs.availability_domains[var.AD - 1],"name")}"
  compartment_id = "${var.compartment_ocid}"
  display_name = "OAMTFInstance"
  image = "${var.InstanceImageOCID[var.region]}"
  shape = "${var.InstanceShape}"

  create_vnic_details {
    subnet_id = "${oci_core_subnet.IDMSubnet.id}"
    display_name = "primaryvnic"
    assign_public_ip = true
    hostname_label = "OAMTFInstance"
  },

  metadata {
    ssh_authorized_keys = "${var.ssh_public_key}"
  }

  timeouts {
    create = "60m"
  }

}
