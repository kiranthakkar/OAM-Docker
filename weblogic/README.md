# Weblogic 10.3.6 on docker

Sample Docker configurations to facilitate installation of weblogic 10.3.6 on docker based on Oracle JDK 1.7.

The certification of WebLogic on Docker does not require the use of any file presented in this repository. Customers and users are welcome to use them as starters, and customize/tweak, or create from scratch new scripts and Dockerfiles.

For more information on the certification, please check the [WebLogic on Docker Certification Whitepaper](http://www.oracle.com/technetwork/middleware/weblogic/overview/weblogic-server-docker-containers-2491959.pdf)  and [WebLogic Blog](https://blogs.oracle.com/WebLogicServer/) for updates.

For pre-built images containing Oracle software, please check the [Oracle Container Registry](https://container-registry.oracle.com/).

##How to build and run

Make sure you have create docker image for Oracle Java 7.

**IMPORTANT:** you have to download the binary of WebLogic and put it in weblogic directory.

$ cd ../weblogic
$ docker build -t oracle/weblogic:11g

## License
To download and run WebLogic 12c Distribution regardless of inside or outside a Docker container, and regardless of the distribution, you must download the binaries from Oracle website and accept the license indicated at that page.

To download and run Oracle JDK regardless of inside or outside a Docker container, you must download the binary from Oracle website and accept the license indicated at that pge.

All scripts and files hosted in this project and GitHub repository required to build the Docker images are, unless otherwise noted, released under [UPL 1.0](https://oss.oracle.com/licenses/upl/) license.

## Copyright
Copyright (c) 2014-2017 Oracle and/or its affiliates. All rights reserved.
