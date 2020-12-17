Small tools

```bash
# Before video
clear; env -i bash --norc --noprofile
export HISTCONTROL=ignorespace
 while read line; do 
   history -s "$line"; 
 done < hist.sav
 !2;!3;!4;!5;!6
```
```bash
# Lesson
mc
which cd
which pwd
man cd
man pwd
cd --help
pwd --help
man ls
ls -i
ls --inode
ls 
ls -w 50
ls -w50
ls --width 50
ls --width=50
ls --width=70 -i
ls -a
ls -la
ls bin/* pybin/*
ls bin/colortest bin/word pybin/count-digraphs pybin/similarity pybin/suffixes
ls M*
ls [Mm]*
ls ?o*
ls [A-Z]*
ls [!A-Z]
ls [!A-Z] -d
touch 'filename with spaces'
ls -1
rm filename with spaces
rm 'filename with spaces'
touch 'filename with spaces'
rm filename\ with\ spaces
echo "$HOME"
echo '$HOME'
touch 'filename with spaces'
ls -i "$HOME/tmp/scratch/filename with spaces"
```

Everything is a file

```bash
cat hello.english
echo "Molo Lizwe" > hello.xhosa
cat hello.xhosa
echo "Chào thế giới" | cat
history > hist.txt
head hist.txt
history | head
history | cut -c8- | head
history | cut -c8- | tr '|' '\n' | head
history | cut -c8- | tr '|' '\n' | sed 's/^ *//' | head
history | cut -c8- | tr '|' '\n' | sed 's/^ *//' | cut -d' ' -f1 | head
history | cut -c8- | tr '|' '\n' | sed 's/^ *//' | cut -d' ' -f1 | sort | uniq -c
history | cut -c8- | tr '|' '\n' | sed 's/^ *//' | cut -d' ' -f1 | sort | uniq -c | sort -nr
ls | egrep '(.)\1' 
wc $(ls | egrep '(.)\1')
cat pop-upgrade.status
diff pop-upgrade.status pop-upgrade.other 
cut -d] -f2- pop-upgrade.status 
diff <(cut -d] -f2- pop-upgrade.status) <(cut -d] -f2- pop-upgrade.other)
```