# FRA RSS

To generate the JSON that the feed is based on, run this command

```sh
scrapy crawl newsroom
```

All the extra stuff you see is hitting stderr. So you should be able to pipe
the output of the command above and get a bunch of one-line jsons in a single
file.

## TODO

- Write a script that converts those JSONs to an RSS feed using `feedgen`.
- Write a shell script for CI to call that script on the output of the command
  above.
- Figure out where to host it.

## Important Files

The only files I edited or created directly in this repository so far are

- `example-page.html`: This is just a snapshot of the page's html that RSS feed
  is constructed from.
- `fra_rss/spiders/newsroom.py`: This is where the spider that scrapes the
  correct HTML elements and converts them into the JSON lives.
- `README.md`: (obvious).

The rest of the files were auto-generated with `poetry` and `scrapy`.
