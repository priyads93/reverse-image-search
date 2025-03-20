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

#### Initialize chromadb database
```bash
chroma run --path /db_path
```

## Modify path details in code base

In line number 33 and line number 40 of image-search.py modify the path to the images folder present in local system

## Code Execution

Execute the code with following command line in terminal

```bash
python3 <full path to the image-search.py>
```