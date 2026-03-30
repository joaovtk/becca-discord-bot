FROM maven

WORKDIR /app
COPY src /app/src
COPY pom.xml /app/pom.xml
RUN mvn clean package -DskipTests
COPY target/beccaapi-0.0.1-SNAPSHOT.jar /app/app.jar

ENTRYPOINT [ "java", "-jar", "app.jar"]