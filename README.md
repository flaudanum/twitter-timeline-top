# Top Twitter users

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
$ python run.py --top 5 --file ./data/tweets.json 
The 5 most present users in the timeline are:

        - François GEUZE        (41 tweets)
        - Benedict Evans        (39 tweets)
        - Le Lab RH     (25 tweets)
        - MIT Tech Review       (25 tweets)
        - Peter Skomoroch       (21 tweets)
```

## Packaging

You may package the application with _setuptools_:

```
python3.9 setup.py sdist
```

This command packages the application into an archive `./dist/top-tweeters-1.0.0.tar.gz`.

## Installation

The application can then be installed as a global script with PyPI:

```
pip3.9 install ./dist/top-tweeters-1.0.0.tar.gz
```

Run the CLI:

```
$ top-tweeters --file top-tweeters/data/tweets.json --top 6
The 6 most present users in the timeline are:

	- François GEUZE	(41 tweets)
	- Benedict Evans	(39 tweets)
	- Le Lab RH	(25 tweets)
	- MIT Tech Review	(25 tweets)
	- Peter Skomoroch	(21 tweets)
	- Ryan Florence	(18 tweets)
```
