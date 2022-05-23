"""Python module with useful functions for data analysis"""
import json
import operator

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def show_classes_distribution(
    dict, plt_name=None, ylabel='persent', figsize=(20, 4), dpi=100
):
    x = np.arange(len(list(dict.keys())))
    width = 0.75

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    rects1 = ax.bar(x, dict.values(), width)

    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(dict.keys())
    plt.title(plt_name)
    plt.show()


def eval_entity_classes_distribution(df, entities_categories):
    entities_categories_counts = {k: 0 for k in entities_categories}

    for i in range(len(df)):
        for j in range(len(df["entities"][i])):
            if df["entities"][i][j]["entity"] in entities_categories:
                entities_categories_counts[df["entities"][i][j]["entity"]] += 1
    return sort_dict(entities_categories_counts)


def eval_intent_classes_distribution(df, intent_classes):
    intent_classes_counts = {k: 0 for k in intent_classes}

    for i in range(len(df)):
        if df["intent"][i] in intent_classes:
            intent_classes_counts[df["intent"][i]] += 1
    return sort_dict(intent_classes_counts)


def sort_dict(dictionary):
    """Sorts dictionary values in reverse order
    """
    return dict(
        sorted(
            dictionary.items(),
            key=operator.itemgetter(1), reverse=True
        )
    )


def eval_persentage(dictionary, maxelems):
    """Evaluates values persents and returns as a dictionary
    """
    return {key: (value / maxelems * 100) for (key, value) in dictionary.items()}


def get_entity_classes(df):
    """Returns unique entities from DataFrame
    """
    unique_entities = set()

    for i in range(len(df)):
        for j in range(len(df["entities"][i])):
            unique_entities.add(df["entities"][i][j]["entity"])

    return list(unique_entities)


def get_intent_classes(df):
    """Returns intent classes from DataFrame
    """
    unique_intents = set()

    for i in range(len(df)):
        unique_intents.add(df["intent"][i])

    return list(unique_intents)


def contains(key, collection):
    """Checks if some value contains in key
    """
    if collection is None:
        return False
    for item in collection:
        if item in key:
            return True
    return False


def get_entity_classes_in_category(key, entities, blocklist=None):
    """Gets all specific values from given entities except that is in blocklist
    """
    items = []
    for i in range(len(entities)):
        if not contains(entities[i], blocklist) and key in entities[i]:
            items.append(entities[i])

    return items
