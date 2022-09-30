# FRA RSS

RSS and Atom feed of the FRA press releases.

- https://fra-rss.nyc3.cdn.digitaloceanspaces.com/rss.xml
- https://fra-rss.nyc3.cdn.digitaloceanspaces.com/atom.xml

## Generation

To scrape the website and put the feeds in a `generated/` directory, call the
`generate.sh` script.

```sh
poetry shell  # For dependencies...
sh generate.sh
```

## TODO

- Add CI.
- Figure out where to host it.

## Important Files

The only files I edited or created directly in this repository so far are

- `example-page.html`: This is just a snapshot of the page's html that RSS feed
  is constructed from.
- `fra_rss/spiders/newsroom.py`: This is where the spider that scrapes the
  correct HTML elements and converts them into the JSON lives.
- `README.md`: (obvious).
- `generate.sh`: Create the Atom and RSS feeds and put them in the `generated` directory.
- `test_server.sh`: Run a test server to verify that the feed work in your local RSS reader.

The rest of the files were auto-generated with `poetry` and `scrapy`. I did
reformat some of Scrapy's auto-generated files with BlacScrapy's auto-generated
files with Black.
