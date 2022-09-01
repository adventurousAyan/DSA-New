#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'getArticleTitles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
# URL for cut and paste:
# https://jsonmock.hackerrank.com/api/articles?author=<authorName>&page=<num>
#
#
import requests
import json


def getArticleTitles(author):
    # Write your code here
    titles = []
    page_count = 1
    total_pages = 0
    base_uri = "https://jsonmock.hackerrank.com/api/articles"
    uri = f"{base_uri}?author={author}&page={page_count}"

    request_data = requests.get(uri)
    content = json.loads(request_data.content)
    total_pages = content.get("total_pages", 0)

    titles_array = content.get("data", [])
    # print(content)
    for item in titles_array:
        # print(item["title"])
        if item.get("title", None):
            titles.append(item["title"])
        elif item.get("story_title", None):
            titles.append(item["story_title"])

    page_count += 1
    while page_count <= total_pages:
        uri = f"{base_uri}?author={author}&page={page_count}"
        # print(uri)
        request_data = requests.get(uri)
        content = json.loads(request_data.content)
        titles_array = content.get("data", [])
        for item in titles_array:
            if item.get("title", None):
                titles.append(item["title"])
            elif item.get("story_title", None):
                titles.append(item["story_title"])
        page_count += 1

    return titles


if __name__ == "__main__":

    author = input()

    result = getArticleTitles(author)
    print(result)
