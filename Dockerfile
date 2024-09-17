FROM --platform=arm64 ubuntu:latest as build
RUN apt-get update
RUN apt-install openjdk-17-jdk -y
COPY . .
RUN apt-get install maven -y
RUN mvn clean-install
FROM openjdk:17-slim
COPY --from=build /target/BeccaTk-1.0-SNAPSHOT.jar app.jar

ENTRYPOINT [ "java", "-jar", "app.jar" ]