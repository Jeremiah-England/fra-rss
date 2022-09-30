import json
import fileinput
from feedgen.feed import FeedGenerator
import os


# See copied example at https://python-feedgen.readthedocs.io/en/latest/
fg = FeedGenerator()
fg.id("https://railroads.dot.gov/newsroom/press-releases")
fg.title("FRA Newsroom Press Releases")
fg.author({"name": "FRA Newsroom"})
fg.link(href="https://railroads.dot.gov/newsroom/press-releases", rel="alternate")
fg.logo(logo="https://railroads.dot.gov/themes/custom/fra/fra-logo%402x.png")
fg.subtitle("Links to press relases from the Federal Railway Administration (FRA).")
fg.language("en")

for line in fileinput.input(encoding="utf-8"):
    entry_json = json.loads(line)
    fe = fg.add_entry(order="append")
    fe.id(entry_json["link"])
    fe.title(entry_json["title"])
    fe.link(href=entry_json["link"])


directory = "generated"
os.makedirs(directory, exist_ok=True)
fg.atom_file(f"{directory}/atom.xml", pretty=True)
fg.rss_file(f"{directory}/rss.xml", pretty=True)
