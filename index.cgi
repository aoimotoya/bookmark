#!/usr/bin/env bash

dir=$(dirname $0)
articles_dir=$dir/articles
misc_dir=$dir/misc
days=7

echo "Content-Type: text/html"
echo

contents="<h2>直近 $days 日間のブックマーク</h2>"
contents=${contents}"<ol>"
contents=${contents}`find $articles_dir -type f -mtime -$days | LANG=C sort -nr | xargs cat | sed -e 's/^\</\<li\>\</g' | sed -e 's/\>$/\>\<\/li\>/g'`
contents=${contents}"</ol>"
contents=${contents}"<h2>過去のブックマーク</h2>"
contents=${contents}"<p>"
contents=${contents}`find articles/ -type f -mtime +$days | wc -l | sed -e 's/[[:blank:]]*//g'`
contents=${contents}" 件</p>"

echo "$contents" | filehame -lDOCUMENT $misc_dir/template.html -

