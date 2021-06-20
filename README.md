# Top Tweeter users

## Dev environment

### Install environment

```
python3.9 -m venv env
python -m pip install -U pip setuptools
pip install -r requirements.txt 
```

### Run tests

In the dev environment:

```
pytest
```

### Running the app

```
$ python main.py --top 5 --file ./data/tweets.json 
The 5 most present users in the timeline are:

        - François GEUZE        (41 tweets)
        - Benedict Evans        (39 tweets)
        - Le Lab RH     (25 tweets)
        - MIT Tech Review       (25 tweets)
        - Peter Skomoroch       (21 tweets)
```

