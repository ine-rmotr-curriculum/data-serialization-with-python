Searching

```bash
# Before presentation
export HISTCONTROL=ignorespace
export LC_ALL=en_US.UTF-8
export TERM=xterm
export PS1='\e[0;32m(\@) \e[0;35m\W\e[0m \!-% '
export PAGER=less
alias head='tee /dev/null|head'
clear
```

```bash
cd ~/git/INE
find . | head -20
find . | tee /dev/null | head
find . | wc -l
find $PWD/bash | wc -l
find . -name '*.csv'
find . -ctime -3 -name '*.ipynb' 
find . -ctime -3 -name '*.ipynb' | grep -v checkpoint
find . -size +5M
locate Unix-Philosophy Text-Manipulation
locate --all ipynb Exceptions 
locate --all ipynb Exceptions INE
find . -name 'demo-steps.md'
grep '^bash..$' /usr/local/share/wordlist-en.txt 
grep -E '^bash.{1,3}$' /usr/local/share/wordlist-en.txt 
grep -E 'bash.{3,4}$' /usr/local/share/wordlist-en.txt 
grep -v '[aeiouy]' /usr/local/share/wordlist-en.txt 
grep PS1 $(find . -name 'demo-steps.md')
ag david 
ag david --pager "less -R"
ag --html david 
ag --py david 
ag --py -s David
ag --py -sl david
```

Filtering

```bash
cd ~/tmp/scratch
grep Ishmael Moby-Dick.txt
grep -n Ishmael Moby-Dick.txt
cat -n Moby-Dick.txt | grep Ishmael
cat -n movie.csv
tac movie.csv
cat -n movie.csv | tac
cat pop-upgrade.log 
grep Ishmael Moby-Dick.txt | cat -n
grep Ishmael Moby-Dick.txt | cat -n | head -n 8
grep Ishmael Moby-Dick.txt | cat -n | head -8
grep Ishmael Moby-Dick.txt | cat -n | head -n -8
grep Ishmael Moby-Dick.txt | cat -n | tail -n8
grep Ishmael Moby-Dick.txt | cat -n | tail -n+8
cat -n Moby-Dick.txt | grep Ishmael | cut -c-6
cat -n Moby-Dick.txt | grep Ishmael | cut -c-6 | paste -s -d+ | bc
cat -n Moby-Dick.txt | grep Ishmael | cut -c-6 | paste -s -d+ 
csvcut -K1 -c4 movie.csv 
csvcut -K1 -c4 movie.csv | paste -s -d+ | bc
echo "($(csvcut -K1 -c4 movie.csv | paste -s -d+))" / $(tail -n+2 movie.csv | wc -l)
echo $(csvcut -K1 -c4 movie.csv | paste -s -d+) / $(tail -n+2 movie.csv | wc -l) | bc
cut -d] -f2- pop-upgrade.status 
cut -c44- pop-upgrade.status 
cat -n movie.csv
cat -n biography.csv 
paste -d, movie.csv biography.csv 
cat -n biography2.csv
paste -d, movie.csv biography2.csv 
join -t, movie.csv biography.csv 
join -t, movie.csv biography2.csv 
join -t, <(sort movie.csv) <(sort  biography2.csv)
unalias head
join -t, <(tail -n+2 movie.csv|sort) <(tail -n+2 biography2.csv|sort)

join -t, <(head -1 movie.csv) <(head -1 biography2.csv)
shuf Moby-Dick.txt | head -5
shuf Moby-Dick.txt | head -5
```

Archiving

```bash
ls -lh Moby*
gzip Moby*
ls -lh Moby*
hexdump -C Moby-Dick.txt.gz | head # 0x1f8b
file Moby-Dick.txt.gz 
gunzip *
ls -lh Moby*
gunzip -c Moby-Dick.txt.gz | head
zcat Moby-Dick.txt.gz | head
ls -lh Moby-Dick.txt
gunzip Moby*
gzip -9 Moby-Dick.txt 
ls -lh Moby-Dickt.txt.gz
gunzip Moby*

bzip2 Moby*
ls -lh Moby*
file *
bzcat Moby-Dick.txt.bz2 | wc
man bzip2
bunzip2 Moby*

xz -v Moby*
ls -lh Moby*  # bz2 better for text
file Moby*
xzcat Moby-Dick.txt.xz | shuf | head -4
unxz *

touch bin/newfile
tar cvf test.tar bin/ pybin/
rm bin/newfile
tar --compare --file=test.tar
tar -df test.tar -C .
tar -rvf test.tar *.csv
tar -t < test.tar 
cat test.tar | tar --list
xz test.tar
xz -l test.tar.xz
tar --xz --create --verbose --file test.tar.xz bin/ pybin/ *.csv
xz -l test.tar.xz 
tar -zcvf test.tgz bin pybin *.csv
# also -J fo xz, -j for bzip2

zip -r test pybin/* bin/* *.csv
unzip -l test.zip 
ls -lh test.zip
zip -Z bzip2 -r test pybin/* bin/* *.csv
ls -lh test.zip
```

