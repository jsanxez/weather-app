Run the application
===================

Using docker:

```
docker build -t <name> .
```

```
docker run -p 80:8000 <name>
```

Or using docker-composer:

```
docker-compose up -d
```

> If docker-compose is not in $PATH variable you can check
> `/usr/lib/docker/cli-plugins/docker-compose` to execute it.

