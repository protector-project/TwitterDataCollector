# DOWNLOAD DATA FROM TWITTER

### Requirements

It is recommended to install an environment management system (e.g., miniconda3) to avoid conflicts with other programs. After installing miniconda3, create the environment `$ENV_NAME` and install the packages from `requirements.txt`:

```
cd $PROJECT_DIR                           # access the folder relative to this project
conda create --name $ENV_NAME python=3.8  # create a python 3.8 environment $ENV_NAME
conda activate $ENV_NAME                  # activate the environment $ENV_NAME
python -m pip install -r requirements.txt # install packages from requirements.txt
python -m spacy download en_core_web_sm   # install spacy en language model
```

Alternatively, you can also install python 3.8 and packages from `requirements.txt` manually. However, there is no guarantee that the package versions will match those from the requirements.


### Usage

In this following we outline (1) how to download Twitter data, and (2) how to run the hate speech detection model on tweets.


##### Download relevant data from Twitter

In order to download Twitter data relevant to the project, then writing it to a file `$OUTPUT_FILEPATH`, just run the command:

`python Main_downloader.py -S $START_DATE -E $END_DATE > $OUTPUT_FILEPATH`

where:
- `$START_DATE` (**required**): the start time for the time period you want tweets from, in the format YYYY-MM-DD
- `$END_DATE` (**required**): the end time for the time period you want tweets from, in the format YYYY-MM-DD

The output file will contain a line per tweet, in a json line format (a sample file is `data/example.jsonl`). Each entry can be stored on a dedicated database in the way you like. The relevant json keys are `id` and `text`. For further information on the data dictionary (key, values) of a tweet json line, please see: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet.

**Additional options**

Useful optional arguments (with a default value) are the following:
- `-L` (default: `en`): The language code of the tweets. Choices are `en` and `it`.
- `-T` (default: `all`): the religious topic of the tweets (i.e., an abstraction of the underlying designed queries). Choices are `all`, `christianity`, `islam`, and `judaism`.

**Example**

`python download_data.py -S 2021-09-20 -E 2021-09-26 -L it -T judaism > my_outputfile.jsonl` will download all the tweets written in **Italian** language related to **Judaism** from **2021-09-20** to **2021-09-26** to the file `my_outputfile.jsonl`.

**Note**: remeber that the Twitter API has a rate limit, and a tweet consumption cap limits the volume of tweets we can retrieve in a given month. Please limit the amount of requests / amount of tweets to download for testing purposes to allow the DH research group to continue working on PROTECTOR and other projects which require the downloading of Twitter data.
