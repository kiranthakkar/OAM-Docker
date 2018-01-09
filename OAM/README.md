# Oracle Access Manager on Docker

Sample Docker configurations to facilitate installation, configuration, and environment setup for DevOps users. This project includes quick start for Oracle Access Manager R2PS3 11.1.2.3.0 based on Oracle Linux 7, Oracle JDK 7 (Server) and Oracle weblogic 10.3.6.

For more information about Oracle Access Manager, please see the [Oracle Access Manager 12.1.2.3.0 Online Documentation](https://docs.oracle.com/cd/E52734_01/index.html).

The certification of Oracle Access Manager on Docker does not require the use of any file presented in this repository. Customers and users are welcome to use them as starters, and customize/tweak, or create from scratch new scripts and Dockerfiles.

For pre-built images containing Oracle software, please check the [Oracle Container Registry](https://container-registry.oracle.com).

The instructions below can also be used to build and run Oracle Access Manager 11.1.2.3.0, based on weblogic 10.3.6.

## Oracle Access Manager(OAM) Docker Image Creation

To build a OAM image you start by building the Oracle Java image and then the Oracle weblogic image.

### Building the Oracle Java (Server JRE) Image

Download the Oracle Server JRE binary into folder `java` and build the image:

        $ cd java
        $ docker build -t oracle/java:7 .

### Building the Oracle weblogic 10.3.6
 
Download the binary of weblogic 10.3.6 into folder `weblogic`.

Build the image:

        $ cd ../weblogic
        $ docker build -t oracle/weblogic:11g

### Building the Oracle Access Manager Image

Download the three binaries for [Oracle Access Manager 11.1.2.3.0](http://www.oracle.com/technetwork/middleware/id-mgmt/downloads/oid-11gr2-2104316.html) for Linux x86-64-bit into folder `OAM`.

If a proxy is needed for the host to access yum.oracle.com during build, then first set up the appropriate environment, e.g.:

        $ export http_proxy=myproxy.example.com:80
        $ export https_proxy=myproxy.example.com:80
        $ export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"

Build the image:

        $ cd OAM
        $ docker build -r oracle/oam:R2PS3
