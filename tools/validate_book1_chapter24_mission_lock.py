#!/usr/bin/env python3
"""Protect the exact Chapter 24 final-chapter mission lock during drafting."""
import re
from validate_book1_chapter24_draft import LOCK, fail, read, validate_common

validate_common()
lock = read(LOCK)
sections = re.findall(r"^## (\d+)\. ", lock, flags=re.MULTILINE)
if sections != [str(i) for i in range(1, 39)]:
    fail(f"mission-lock sections are not exactly 1-38: {sections}")
if lock.count("### Movement ") != 4:
    fail("mission lock must contain exactly four movement blueprints")
for phrase in (
    "# Chapter 24 Mission Lock — The Terms of Return", "15:04:44 EDT / 00:34:44 IST",
    "Julie O'Donnell close third, past tense, for the entire chapter", "No cutaway is authorized",
    "Acceptable range:** **3,150–3,450 words", "Hard maximum:** **3,583 words",
    "exactly four causal movements", "independent source-integrity and evidence-architecture practice",
    "permits future contact outside rank and command", "Elias controls future contact and technical participation",
    "MPD-901441` through `MPD-901447", "136 sealed / 47 incomplete / 311 excluded", "LSS-SL-90418",
    "original 02:14 human operator", "human constructor of the borrowed request path",
    "Sterling's knowledge, intent, direction, or command", "No Chapter 25 is authorized or implied",
):
    if phrase.lower() not in lock.lower():
        fail(f"mission lock missing {phrase}")
print("PASS: Chapter 24 mission lock remains exact while the first draft stays non-canon")
