iconv -f GBK -t UTF-8 *.md > *.md
git add .
git commit -m "update code"
git push