# MovieRecommendation
How to incrementally update your ML model in an automated way as new training data becomes available
Fitting and serving your machine learning (ML) model is one thing, but what about keeping it in shape over time?

Let's say we got a ML model that has been put in production and is actively serving predictions. Simultaneously, we got new training data that becomes available in a streaming way while users use the model. Incrementally updating the model with new data can improve the model, whilst it also might reduce model drift. However, it often comes with additional overhead. Luckily, there are tools that allow you to automate many parts of this process. 

This repository takes on the topic of incrementally updating a ML model as new data becomes available. It mainly leans on three nifty tools, being Kafka, Airflow, and MLFlow.

The corresponding walkthrough/post on Medium lays out the workings of this repo step-by-step.



Had a similar problem and what worked for me was deleting containers and volumes

List all containers by id:

docker container ls -qa
run this to each container:

docker container rm [id]
And same with volumes:

docker volume ls
docker volume rm [VolumeName]

/opt/homebrew/bin/postgres

docker-compose up --build --force-recreate

