# Use a imagem base com JDK 22
FROM eclipse-temurin:22-jdk-alpine AS build

# Instalar Maven
RUN apk add --no-cache maven

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo pom.xml e o código-fonte para o contêiner
COPY . .

# Expor a porta que a aplicação vai usar (se necessário)
EXPOSE 8080

# Executar o Maven para compilar o projeto
RUN mvn clean install

#COPY --from=build /target/BeccaTk-1.0-SNAPSHOT.jar /app/BeccaTk.jar

# Expor a porta necessária
EXPOSE 8080

# Comando para executar a aplicação
ENTRYPOINT ["java", "-jar", "/target/BeccaTk.jar"]