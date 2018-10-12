
to get the most accurate results, make sure to rebuild your coin daemon with the following value changed:
P2P_LOCAL_WHITE_PEERLIST_LIMIT from 1000 to 10000
in file /src/CryptoNoteConfig.h on line 108-ish

Build the image using the following command

```bash
$ docker build -t elyamap-app .
```

Run the Docker container using the command shown below.

```bash
docker run -d --name elyamap --restart unless-stopped -p 8081:8050 elyamap-app
```

The application will be accessible at http://127.0.0.1:8081