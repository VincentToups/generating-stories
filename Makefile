data/aita.txt: grab_subreddit.py
	mkdir -p data
	python3 grab_subreddit.py -s AmItheAsshole -n 50 -o data/aita.txt

