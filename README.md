Build the image using the following command

```bash
$ docker build -t elyamap-app .
```

Run the Docker container using the command shown below.

```bash
docker run -d --name elyamap --restart unless-stopped -p 8081:8050 elyamap-app
```

The application will be accessible at http://127.0.0.1:8081