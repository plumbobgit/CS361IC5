import pytest
import wordCount


def test_palindromeness():
    value = wordCount.wordCounts("Hey there feller")
    assert value == '3'
