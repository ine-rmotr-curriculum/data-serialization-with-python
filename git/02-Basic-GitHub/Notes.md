## Preparing

1. `cd ~/git/git-INE`
1. `docker build . -t ine.git`
1. `docker run -it ine.git bash`
---

## Cloning repositories

```bash
# View https://github.com/DavidMertz/INE-Fractal/tree/main
git clone https://github.com/DavidMertz/INE-Fractal.git
cd INE-Fractal
git branch
git branch -a
git checkout -b optimization origin/optimization
git branch -a
git checkout --detach
git fetch origin '+refs/heads/*:refs/heads/*'
git checkout optimization
tree
git checkout main
tree
# Edit README.md at website
git pull
git checkout -B student-branch
nano README.md 
git add README.md 
git commit -m "Modify README"
git push
git push --set-upstream origin student-branch
# Fail on username/password
```

## Creating an account

Locally:

```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
# Copy key to be ready to paste it
# Create an account at https://github.com
git clone git@github.com:DavidMertz/INE-Fractal.git
git checkout --detach
git fetch origin '+refs/heads/*:refs/heads/*'
git checkout -B student-branch
nano README.md 
git add README.md 
git commit -m "Modify README"
git push
git push --set-upstream origin student-branch
# View the change at website
```

## Creating a repository

* Create a repository through GitHub.com website

```bash
git remote add origin git@github.com:INE-Student/Fractal.git
git branch -M main
git push -u origin main
```

## Forking a repository

```
# https://github.com/DavidMertz/coalesce
git clone
```