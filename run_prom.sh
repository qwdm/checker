
#docker run \
#    -d \
#    -p 9090:9090 \
#    -v `pwd`/prometheus.yml:/etc/prometheus/prometheus.yml \
#    prom/prometheus


docker run \
    -d \
    --network="host" \
    -v `pwd`/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
    
docker run -d -p 9091:9091 prom/pushgateway
