#! /usr/bin/env python
# -*- coding: utf-8 -*-
CONFIDENCE_THRESHOLD = 2  # The minimum level of confidence necessary to return the answer
OTHER_MATCH_DEMPHASIZR = 3  # The amount by which to deemphasize subsequent occurences of a word after the first


def get_best_answer(pages):
    """
    Takes a list of pages to consider and returns the best one
    as long as it's above the minimum confidence threshold.
    """
    top_page = {"score": 0}
    for page in pages:
        if page["score"] > top_page["score"]:
            top_page = page

    if top_page["score"] < CONFIDENCE_THRESHOLD:
        return None
    else:
        return top_page
