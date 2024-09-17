# Use a imagem base com JDK 22
FROM eclipse-temurin:22-jdk-alpine

# Instalar Maven
RUN apk add --no-cache maven

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo pom.xml e o código-fonte para o contêiner
COPY pom.xml .
COPY src ./src

# Executar o Maven para compilar o projeto
RUN mvn clean package

# Expor a porta necessária
EXPOSE 8080

# Comando para executar a aplicação
CMD ["java", "-jar", "target/BeccaTk.jar"]
