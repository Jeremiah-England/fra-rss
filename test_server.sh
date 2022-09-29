echo "Serving at port http://localhost:9000

These feed links should work on your local machine while this is running:

http://localhost:9000/atom.xml
http://localhost:9000/rss.xml
"

python -m http.server 9000 --directory generated
