#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup


def get_soup(url):
    """
    Creates a BeautifulSoup object for a particular url.
    Returns the BeautifulSoup object.
    """
    site = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    req = urllib2.Request(site, headers=headers)
    html = urllib2.urlopen(req)

    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_headline(url):
    """
    Scrapes the social media headline of a particular url.
    Uses social meta tags (Open Graph / Twitter) to consistently find it.
    Returns the headline or None if no headline could be found.
    """
    soup = get_soup(url)

    prop_regex = re.compile('^(og|twitter)(\:text)?\:title$')
    meta_tag = soup.find("meta", {"name": prop_regex})
    if not meta_tag:
        meta_tag = soup.find("meta", {"property": prop_regex})

    if meta_tag:
        return meta_tag["content"]
    else:
        return None
