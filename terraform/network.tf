resource "oci_core_virtual_network" "IDMVCN" {
  cidr_block = "10.1.0.0/16"
  compartment_id = "${var.compartment_ocid}"
  display_name = "IDMVCN"
  dns_label = "IDMvcn"
}

resource "oci_core_internet_gateway" "IDMIG" {
  compartment_id = "${var.compartment_ocid}"
  display_name = "IDMIG"
  vcn_id = "${oci_core_virtual_network.IDMVCN.id}"
}

resource "oci_core_route_table" "IDMRT" {
  compartment_id = "${var.compartment_ocid}"
  vcn_id = "${oci_core_virtual_network.IDMVCN.id}"
  display_name = "IDMRouteTable"
  route_rules {
    cidr_block = "0.0.0.0/0"
    network_entity_id = "${oci_core_internet_gateway.IDMIG.id}"
  }
}

resource "oci_core_subnet" "IDMSubnet" {
  availability_domain = "${lookup(data.oci_identity_availability_domains.ADs.availability_domains[var.AD - 1],"name")}"
  cidr_block = "10.1.20.0/24"
  display_name = "IDMSubnet"
  dns_label = "IDMsubnet"
  security_list_ids = ["${oci_core_virtual_network.IDMVCN.default_security_list_id}"]
  compartment_id = "${var.compartment_ocid}"
  vcn_id = "${oci_core_virtual_network.IDMVCN.id}"
  route_table_id = "${oci_core_route_table.IDMRT.id}"
  dhcp_options_id = "${oci_core_virtual_network.IDMVCN.default_dhcp_options_id}"
}
