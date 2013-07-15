CH="information"

echo "Split Author.csv..."
perl split_author.pl ../../data/Author.csv

echo "Start to detect chinese..."
perl show_chinese.pl ../../data/Author.csv.aid ../../data/Author.csv.name ${CH}/last.less ${CH}/token.all ${CH}/last.ban ${CH}/token.ban | perl show_p.pl > ../../buff/chinese_author.less

perl show_chinese.pl ../../data/Author.csv.aid ../../data/Author.csv.name ${CH}/last.more ${CH}/token.all ${CH}/last.ban ${CH}/token.ban | perl show_p.pl > ../../buff/chinese_author.more
