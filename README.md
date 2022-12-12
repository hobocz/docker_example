#### A simple example project meant to demonstrate using Docker.
#### It includes GitHub to DockerHub integration as part of CI/CD.
[python 3.10.8, Flask 2.2.2, mysql-connector-python 8.0.31]

This is a basic example, and *not meant to display complex
functionality*. It is only a starting point, and attempts to
demonstrate an understanding of Docker concepts.

- 2 containers managed with Docker Compose
- One container runs MySQL
- The other container populates, queries, and displays DB data to a web page using Flask