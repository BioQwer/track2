RAWDIR:=../data
CSV = data/Author.csv data/Paper.csv data/PaperAuthor.csv

all: final.csv 

final.csv: buff/main.csv buff/track2_cn.dump
	./post/new_build_pair_cn_athr.py buff/track2_cn.dump  buff/main_cn.csv
	./main/scripts/mergecsv.py buff/main_cn.csv buff/main.csv buff/pre_final.csv
	./post/cascate_loose.py data/PaperAuthor.csv data/Author.csv buff/pre_final.csv buff/final_loose_1.csv
	./post/new2_cascate_loose.py data/PaperAuthor.csv data/Author.csv buff/final_loose_1.csv buff/final_loose.csv
	./post/group_same_ppr.py data/Paper.csv buff/same_ppr_ttl
	./post/find_link.py buff/same_ppr_ttl data/PaperAuthor.csv data/Author.csv buff/out_partial
	./post/ppr_ttl.py  buff/final_loose.csv buff/out_partial buff/track2_cn.dump final.csv
	./post/kickout.py data/Author.csv final.csv final.csv
	cp final.csv ../buff/main1.csv

buff/main.csv: buff/track2.dump
	./main/scripts/track2.py -r buff/main_lev.csv buff/track2.dump buff/main.csv

buff/track2.dump: buff/chinese_author.less $(CSV)
	python pre/build_all_info_athr.py data/Author.csv data/Paper.csv data/PaperAuthor.csv buff/chinese_author.less buff/track2.dump

buff/track2_cn.dump: buff/chinese_author.more $(CSV)
	python pre/build_all_info_cn_athr.py data/Author.csv data/Paper.csv data/PaperAuthor.csv buff/chinese_author.more buff/track2_cn.dump

# Difference to .less version is inclusion of TW.raw & KR.raw
buff/chinese_author.more: $(CSV)
	mkdir -p buff
	perl show_chinese.pl data/Author.csv.aid data/Author.csv.name ${CH}/last.more ${CH}/token.all ${CH}/last.ban ${CH}/token.ban | perl show_p.pl > buff/chinese_author.more


buff/chinese_author.less: $(CSV)
	mkdir -p buff
	perl show_chinese.pl data/Author.csv.aid data/Author.csv.name ${CH}/last.less ${CH}/token.all ${CH}/last.ban ${CH}/token.ban|perl show_p.pl > buff/chinese_author.less

data/Author.csv.aid data/Author.csv.name data/Author.csv.affilia: data/Author.csv pre/kddcup2013wschin_less/split_author.pl
	perl pre/kddcup2013wschin_more/split_author.pl data/Author.csv

$(CSV):
	mkdir -p data
	# Copy data files without header line
	tail -n +2 $(RAWDIR)/Author.csv > data/Author.csv
	tail -n +2 $(RAWDIR)/Paper.csv > data/Paper.csv
	tail -n +2 $(RAWDIR)/PaperAuthor.csv > data/PaperAuthor.csv
	chmod +w data/*

clean:
	rm -rf buff/* data/* pre/kddcup2013wschin_more/kdd2013/Author.csv* pre/kddcup2013wschin_more/Author.csv*  main/kdd/__pycache__/ post/kdd/__pycache__/

cleanclean:
	make clean
	rm -f final.csv
