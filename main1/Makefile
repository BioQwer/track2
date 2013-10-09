RAWDIR:=../data
CSV = ${RAWDIR}/Author.csv ${RAWDIR}/Paper.csv ${RAWDIR}/PaperAuthor.csv

all: final.csv 

final.csv: buff/main.csv buff/track2_cn.dump
	./post/new_build_pair_cn_athr.py buff/track2_cn.dump  buff/main_cn.csv
	./main/scripts/mergecsv.py buff/main_cn.csv buff/main.csv buff/pre_final.csv
	./post/cascate_loose.py ${RAWDIR}/PaperAuthor.csv ${RAWDIR}/Author.csv buff/pre_final.csv buff/final_loose_1.csv
	./post/new2_cascate_loose.py ${RAWDIR}/PaperAuthor.csv ${RAWDIR}/Author.csv buff/final_loose_1.csv buff/final_loose.csv
	./post/group_same_ppr.py ${RAWDIR}/Paper.csv buff/same_ppr_ttl
	./post/find_link.py buff/same_ppr_ttl ${RAWDIR}/PaperAuthor.csv ${RAWDIR}/Author.csv buff/out_partial
	./post/ppr_ttl.py  buff/final_loose.csv buff/out_partial buff/track2_cn.dump final.csv
	./post/kickout.py data/Author.csv final.csv final.csv
	cp final.csv ../buff/main1.csv

buff/main.csv: buff/track2.dump
	./main/scripts/track2.py -r buff/main_lev.csv buff/track2.dump buff/main.csv

buff/track2.dump: buff/chinese_author.less $(CSV)
	python pre/build_all_info_athr.py ${RAWDIR}/Author.csv ${RAWDIR}/Paper.csv ${RAWDIR}/PaperAuthor.csv buff/chinese_author.less buff/track2.dump

buff/track2_cn.dump: buff/chinese_author.more $(CSV)
	python pre/build_all_info_cn_athr.py ${RAWDIR}/Author.csv ${RAWDIR}/Paper.csv ${RAWDIR}/PaperAuthor.csv buff/chinese_author.more buff/track2_cn.dump

# Difference to .less version is inclusion of TW.raw & KR.raw
buff/chinese_author.more: $(CSV)
	mkdir -p buff
	perl pre/show_chinese.pl data/Author.csv.aid data/Author.csv.name ${CH}/last.more ${CH}/token.all ${CH}/last.ban ${CH}/token.ban | perl pre/show_p.pl > buff/chinese_author.more


buff/chinese_author.less: $(CSV)
	mkdir -p buff
	perl pre/show_chinese.pl data/Author.csv.aid data/Author.csv.name ${CH}/last.less ${CH}/token.all ${CH}/last.ban ${CH}/token.ban|perl pre/show_p.pl > buff/chinese_author.less

data/Author.csv.aid data/Author.csv.name data/Author.csv.affilia: data/Author.csv pre/split_author.pl
	perl pre/split_author.pl ${RAWDIR}/Author.csv

$(CSV):
	mkdir -p data

clean:
	rm -rf buff/* data/*  main/kdd/__pycache__/ post/kdd/__pycache__/

cleanclean:
	make clean
	rm -f final.csv
