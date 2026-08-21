# MLOps-US-Visa-Prediction-Project

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Data link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset

## Git commands 

```bash
git add .

git commit -m "message"

git push origin main
```

## How to run?

```bash
python -m venv myenv
```

```bash
.\myenv\Scripts\activate.ps1
```

```bash
pip install -r requirements.txt
```

## Workflows

1. update constants
2. update entity
3. update configuration for data ingestion
4. data access
5. components
6. pipeline

## AWS CICD Deployment with Github Actions

### 1. Login to AWS Console

### 2. Create IAM user for deployment
```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

### 3.Create ECR repo to store/save docker image
```bash
- Save the URI: 315865595366.dkr.ecr.ap-south-1.amazonaws.com/visarepo
```

### 4.Create EC2 Machine(Ubuntu)

### 5. Open EC2 and Install Docker in EC2 machine
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

### 6.Configure EC2 as self hosted runner
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

### 7.Set Github Secrets
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO