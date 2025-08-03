#!/bin/bash
echo "=== Deliver Stage Started ==="
java -jar target/springboot-maven-demo-1.0-SNAPSHOT.jar &
echo "Application running on http://$(hostname -I | awk '{print $1}'):8080/hello"
echo "=== Deliver Stage Completed ==="
