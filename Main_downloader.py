import argparse
import os

from dotenv import load_dotenv
from Downloader import download_tweets

load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-S",
        "--start_date",
        type=str,
        required=True,
        help="The start time for the time period you want tweets from, in the format YYYY-MM-DD.",
    )
    parser.add_argument(
        "-E",
        "--end_date",
        type=str,
        required=True,
        help="The end time for the time period you want tweets from, in the format YYYY-MM-DD.",
    )
    parser.add_argument(
        "-L",
        "--lang_code",
        type=str,
        required=False,
        default="en",
        help="The language of the tweets. Choices: ['en', 'it'].",
    )
    parser.add_argument(
        "-T",
        "--topic",
        type=str,
        required=False,
        default="all",
        help="The religious topic of the tweets. Choices: ['all', 'christianity', 'islam', 'judaism'].",
    )
    parser.add_argument(
        "-C",
        "--category",
        type=int,
        required=False,
        default=0,
        help="The subquery of interest. Choices: [0: None; 1: Religion; 2: Adherent; 3: Scripture; 4: Branch and adherent].",
    )
    args = parser.parse_args()

    download_tweets(
        args.start_date,
        args.end_date,
        args.lang_code,
        os.environ.get("BEARER_TOKEN"),
        args.topic,
        args.category,
    )
