https://www.youtube.com/watch?v=K9AnJ9_ZAXE



## Installing docker-compose manually:
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-darwin-aarch64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose


curl -LfO "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"   #one-time
cd /Users/anshul_jain/Data/Personal/interview_prep/interviewee/17_airflow   
cd airflow_docker
docker-compose up airflow-init  #one-time
docker-compose up
Terminate: ( Window + . )
