# Java 1.7 Docker image

Build a Docker image containing Oracle Java (Server JRE specifically).

The Oracle Java Server JRE provides the same features as Oracle Java JDK commonly required for Server-side Applications (i.e. Java EE application servers). For more information about Server JRE, visit the Understanding the Server [JRE blog entry](https://blogs.oracle.com/java-platform-group/understanding-the-server-jre) from the Java Product Management team.

## Java 7

[Download JDK 7](http://download.oracle.com/otn/java/jdk/7u80-b15/jdk-7u80-linux-x64.tar.gz) .tar.gz file and copy it inside java directory.

	$ cd java
	$ docker build -t oracle/java:7 . 
