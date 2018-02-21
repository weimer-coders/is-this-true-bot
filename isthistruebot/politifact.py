#! /usr/bin/env python
# -*- coding: utf-8 -*-
from scraper import get_soup
from evaluator import OTHER_MATCH_DEMPHASIZR
import urllib
import time


def search_pf(headline):
    """
    Searches PolitiFact for a particular headline and returns the results.
    """
    query = {
        "q": headline
    }
    query_string = urllib.urlencode(query)
    url = "http://www.politifact.com/search/statements/?" + query_string

    search_soup = get_soup(url)
    results = search_soup.findAll("li", "search-results__item")

    pages = []
    for result in results:
        link = "http://www.politifact.com" + result.find("a", "search-results__link")['href']

        page = scrape_pf(link, headline)
        pages.append(page)
        time.sleep(3)

    return pages


def scrape_pf(url, search):
    """
    Scrapes the headline and answer from a PolitiFact fact check.
    Returns a data dictionary with the link, headline, answer, generated score, and source.
    """
    soup = get_soup(url)

    headline = soup.find("meta", {"name": "twitter:title"})["content"]
    answer = soup.find("div", {"class": "meter"}).a.img["alt"]

    score = get_pf_score(
        search,
        title_text=soup.find("h1", {"class": "article__title"}).get_text().strip(),
        statement_text=soup.find("div", {"class": "statement__text"}).get_text().strip(),
        article_text=soup.find("div", {"class": "article__text"}).get_text().strip(),
        sources_text=soup.find("div", {"class": "widget__content"}).get_text().strip()
    )

    return {
        "link": url,
        "headline": headline,
        "answer": answer,
        "score": score,
        "source": "@PolitiFact"
    }


def get_pf_score(search, title_text="", statement_text="", article_text="", sources_text=""):
    """
    Calculates a score based on the presence of a certain set of words in a given text.
    The score gives unique apparances more weight than each appearance of that particular word afterward.
    The score gives seperate weights for each section in which these words appear.
    The score considers the original length of the search query as well.
    Returns a generated score.
    """
    search_words = search.lower().split()
    words_length = len(search_words)

    all_text = [
        {
            "NAME": "title_text",
            "WEIGHT": 10,
            "content": title_text,
            "uniques": 0,
            "other_matches": 0
        },
        {
            "NAME": "statement_text",
            "WEIGHT": 4,
            "content": statement_text,
            "uniques": 0,
            "other_matches": 0
        },
        {
            "NAME": "article_text",
            "WEIGHT": 1,
            "content": article_text,
            "uniques": 0,
            "other_matches": 0
        },
        {
            "NAME": "sources_text",
            "WEIGHT": 6,
            "content": sources_text,
            "uniques": 0,
            "other_matches": 0
        }
    ]

    score = 0.0
    for text in all_text:
        search_text = text["content"].split()
        for word in search_words:
            matches = search_text.count(word)
            if matches > 0:
                text["uniques"] = 1.0
            if matches > 1:
                text["other_matches"] += matches - 1.0
        uniques_score = ((text["uniques"]/words_length) * text["WEIGHT"])
        other_matches_score = ((text["other_matches"]/words_length) * (text["WEIGHT"]/OTHER_MATCH_DEMPHASIZR))
        score += uniques_score + other_matches_score
    return score
