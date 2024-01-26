# Http_server
HTTP server created with 2 parameter m &amp; n with get using flask app python

# Create a docker image
docker build -t httpserver .
# Run the container and map the port 8080 of host with port 8080 of docker image.
docker run -p 8080:8080 httpserver
