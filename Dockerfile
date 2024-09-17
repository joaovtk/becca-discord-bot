FROM --platform=arm64 ubuntu:latest as build
RUN apt-get update
COPY . .
RUN apt-get install maven -y
FROM openjdk:11-jre
RUN mvn clean-install

COPY --from=build /target/BeccaTk-1.0-SNAPSHOT.jar app.jar

ENTRYPOINT [ "java", "-jar", "app.jar" ]