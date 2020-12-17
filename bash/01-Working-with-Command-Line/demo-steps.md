Create a *fresh* shell without my customizations:

```bash
clear; \
env -i bash --norc --noprofile \
    --init-file <(cat /dev/null > ~/.bash_history)
```

Basic file operations:

```bash
cd /home/dmertz/tmp/scratch
ls
ls -l
ls --help
ls ..
ls ../bin
cp -rv ../bin .
ls -l bin
chmod +x bin/colortest
bin/colortest
cat bin/word
bin/word   # denied
chmod +x bin/*
bin/word
bin/word bash.*
mkdir pybin
mv bin/suffixes bin/similarity pybin/
pybin/similarity bash back
tree .
touch test/file1
touch test/file2
cp count-digraphs pybin/
touch pybin/count-digraphs
ls -l pybin
ls -l count-digraphs
touch -d "3 hours ago" pybin/similarity 
ls -l pybin
rm test/*
rmdir test
unzip regex.zip
tree regex
rm -rfv regex
wc bin/* pybin/* Moby-Dick.txt
wc -c Preface-snapshot.pdf regex.zip 
```

Terminal operations

```bash
export LC_ALL=en_US.UTF-8
export TERM=xterm
tree
PS1="\w/> "
PS1="(\D{%Y-%m-%d} \t) \u [\W]$ "
export PS1="\e[0;32m(\@) \e[0;35m\W\e[0m % "
clear
less Moby-Dick.txt
export PAGER=less
man cp
whoami
hostname
pwd
which bash
which python
which python3
export PATH=$PATH:$PWD/bin
echo $PATH
which count-digraphs
MAX=10 count-digraphs Moby-Dick.txt 
echo "she sells sea shells"
echo "she sells sea shells" | count-digraphs
count-digraphs bin/* pybin/* | head -10
```

Affordances

```bash
# Before video
clear; env -i bash --norc --noprofile --init-file <(cat /dev/null > ~/.bash_history)
export HISTCONTROL=ignorespace
 while read line; do 
   history -s "$line"; 
 done < hist.sav
 !2;!3;!4;!5;!6
 
# Lesson
export HISTCONTROL=ignorespace
history 
csv<tab><tab>l<tab> m<tab>
<up><ctrl-left><ctrl-left><ctrl-k>bt<tab>
... csvlook btc-prices.csv | less
<up>
... csvlook btc-prices.csv | tail -5
 history
!16  # date
<up> # date
!11:p
<up>
echo "she sells sea shells by the sea shore"
 history | grep PS1
!4:p
<up>
export PS1='\e[0;32m(\@) \e[0;35m\W\e[0m \!-% '
!10:p  # MAX=10 ...
<up>
... MAX=10 count-digraphs Moby-Dick.txt
<ctrl-a><ctrl-right><ctrl-right><ctrl-u><ctrl-e>
count-digraphs Moby-Dick.txt | wc -l
echo $HOME
echo ~
cd ~/tmp/
cd scratch
cd -
cd -
vim ~/.bashrc  # discuss
```