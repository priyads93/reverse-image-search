## Prerequisites

Please install following on local host machine

| Package                                                                      | Version |
| ---------------------------------------------------------------------------- | ------- |
| [python3](https://www.python.org/downloads/release/python-3100/)              | 3.10.0  |
| [chromadb](https://docs.trychroma.com/docs/overview/getting-started)         |         |


## Project setup

```bash
$ pip install -r /path/to/requirements.txt
```

## pg-vector extension for postgreSQL (in local)

```bash
git clone https://github.com/pgvector/pgvector.git

cd pgvector
make
sudo make install
```

## DB Initialization

1. Download postgresql server in local [postgresql download](https://www.postgresql.org/download/)
2. Start the server and create database by following the steps here [createdb](https://www.postgresql.org/docs/current/tutorial-createdb.html)
3. Create extension for pg-vector and add table using the 'db-init.sql' script

## Steps to Run In Local as REST API

1. Create .env file along with the following details

```bash
DB_USER_NAME=<db-user-name>
DB_NAME=<db-name>
DB_HOST_NAME=<db-host-name>
```

Execute the code with following command line in terminal

```bash
python3 <full path to the image_embeddings_api.py>
```

1. REST service will be up and running in 'localhost:5000'

2. Create embeddings for the images using the following input in post method
```bash
{
    
    "id": <valid-uuid>,
    "url": <image-url>
}
```

3. Get the related images using embedding search using the get method with query params
```bash
http://127.0.0.1:5000/?image_url=<image-url>
```

## Steps to Seed Data

1. Create a csv file along with id -> uuid format, Url -> link to the image file
2. Save the csv file as "seed_data.csv" and then trigger the "initial_image_loading_from_csv.py" file from local. (DB configuration is mandatory for this task to insert data in DB)


## Steps to Run In Local as Python file
#### Initialize chromadb database
```bash
chroma run --path /db_path
```

## Code Execution

Execute the code with following command line in terminal

```bash
python3 <full path to the image-search.py>
```


## Reference Link
https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#image-text-models


