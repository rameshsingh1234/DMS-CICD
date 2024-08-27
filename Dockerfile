# Use the official SonarQube 9.0 image as the base
FROM sonarqube:9.0-community


# Set the JAVA_HOME environment variable to use Java 1
# Expose the SonarQube port
EXPOSE 9000

# Entry point to start SonarQube
ENTRYPOINT ["./bin/run.sh"]
