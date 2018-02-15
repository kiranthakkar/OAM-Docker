variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "region" {}

variable "compartment_ocid" {}
variable "ssh_public_key" {}
variable "ssh_private_key" {}

# Choose an Availability Domain
variable "AD" {
    default = "1"
}

# Gets a list of Availability Domains
data "oci_identity_availability_domains" "ADs" {
    compartment_id = "${var.tenancy_ocid}"
}

variable "InstanceShape" {
    default = "VM.Standard1.2"
}

variable "InstanceImageOCID" {
    type = "map"
    default = {
        // Oracle-provided image "Oracle-Linux-7.4-2017.12.18-0"
        // See https://docs.us-phoenix-1.oraclecloud.com/Content/Resources/Assets/OracleProvidedImageOCIDs.pdf
        us-phoenix-1 = "ocid1.image.oc1.phx.aaaaaaaasc56hnpnx7swoyd2fw5gyvbn3kcdmqc2guiiuvnztl2erth62xnq"
        us-ashburn-1 = "ocid1.image.oc1.iad.aaaaaaaahglw45opiuf6zrbhyuywh7lv5nxsxqbm4yznjwkac6zkapg6zi4a"
        eu-frankfurt-1 = "ocid1.image.oc1.eu-frankfurt-1.aaaaaaaayxmzu6n5hsntq4wlffpb4h6qh6z3uskpbm5v3v4egqlqvwicfbyq"
    }
}

 # Gets a list of vNIC attachments on the instance
data "oci_core_vnic_attachments" "InstanceVnics" {
    compartment_id = "${var.compartment_ocid}"
    availability_domain = "${lookup(data.oci_identity_availability_domains.ADs.availability_domains[var.AD - 1],"name")}"
    instance_id = "${oci_core_instance.OAMTFInstance.id}"
}

# Gets the OCID of the first (default) vNIC
data "oci_core_vnic" "InstanceVnic" {
    vnic_id = "${lookup(data.oci_core_vnic_attachments.InstanceVnics.vnic_attachments[0],"vnic_id")}"
}

variable "DBSize" {
    default = "512" // size in GBs
}

# DBSystem specific 
variable "DBNodeShape" {
    default = "VM.Standard1.2"
}

variable "CPUCoreCount" {
    default = "2"
}

variable "DBEdition" {
    default = "ENTERPRISE_EDITION"
}

variable "DBAdminPassword" {
    default = "QWaszx12##"
}

variable "DBName" {
    default = "IDMdb"
}

variable "DBVersion" {
    default = "11.2.0.4"
}

variable "DBDisplayName" {
    default = "IDMDB"
}

variable "DBDiskRedundancy" {
    default = "HIGH"
}

variable "DBNodeDisplayName" {
    default = "MyTFDatabaseNode0"
}

variable "DBNodeDomainName" {
    default = "example.com"
}

variable "DBNodeHostName" {
    default = "IDMDB"
}

# Define existing bastion host
variable "BastionHost" {
    default = "129.146.26.52"
}

variable "HostUserName" {
    default = "opc"
}

variable "NCharacterSet" {
	default = "AL16UTF16"
}

variable "CharacterSet" {
	default = "AL32UTF8"
}

variable "DBWorkload" {
	default = "OLTP"
}

variable "PDBName" {
	default = "idm"
}

variable "DataStorageSizeInGB" {
	default = "512"
}

variable "LicenseModel" {
	default = "LICENSE_INCLUDED"
}

variable "NodeCount" {
	default = "1"
}

