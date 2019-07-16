# es restore & dump (python version)

## preparation

### install library

```
pip install elasticsearch
```

### launch elasticsearch

```
docker-compose up
```

### load data

```
sh setup_data.sh
```

## running

### dump index

```
python backup.py
```

### restore index

```
python restore.py
```

### delete snapshot & repository

```
python delete_backup.py
```
