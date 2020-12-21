Retrieving data from the internet

```bash
ping www.gnu.org
ping -c3 gnosis.cx
wget https://www.gnu.org/software/wget/manual/wget.txt
wget -r https://www.gnosis.cx/cleaning/stats/
tree www.gnosis.cx/
wget -r -e robots=off https://www.gnosis.cx/cleaning/stats/
wget -rce robots=off https://www.gnosis.cx/cleaning/stats/
curl https://www.gnosis.cx/cleaning/multicsv/2000-01-[01-04].csv > data.csv
less data.csv
rm data.csv
curl https://www.gnosis.cx/cleaning/multicsv/2000-01-[01-04].csv | grep '933,Alice'
curl --silent https://www.gnosis.cx/cleaning/multicsv/2000-01-[01-04].csv | grep '933,Alice'
lynx https://www.gnosis.cx/cleaning/
lynx -dump https://www.gnosis.cx/cleaning/multicsv/
lynx -dump -listonly -nonumbers https://www.gnosis.cx/cleaning/multicsv/
lynx -dump -listonly -nonumbers https://www.gnosis.cx/cleaning/multicsv/ | grep 2000
links https://www.gnosis.cx/cleaning/
links -dump https://www.gnosis.cx/cleaning/multicsv/
scp gnosis@gnosis.cx:~/www/cleaning/morley.dat .
scp Moby-Dick.txt gnosis@gnosis.cx:~/www/cleaning/
rsync -avz /home/dmertz/git/sample-data/multicsv gnosis@gnosis.cx:~/www/cleaning
touch /home/dmertz/git/sample-data/multicsv/TEST
rsync -avz /home/dmertz/git/sample-data/multicsv gnosis@gnosis.cx:~/www/cleaning
rm /home/dmertz/git/sample-data/multicsv/TEST
rsync -avz gnosis@gnosis.cx:~/www/cleaning/multicsv .
```