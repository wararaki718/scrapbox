FROM openjdk:8-jre

VOLUME /tmp

COPY build/libs/sample-docker-1.0-SNAPSHOT.jar /work/app.jar

WORKDIR /work
CMD ["java", "-Djava.security.egd=file:/dev/./urandom","-jar","app.jar"]
