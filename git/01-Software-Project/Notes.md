Preparing

1. `cd ~/git/git-INE`
1. `docker build . -t ine.git`
1. `docker run -it ine.git bash`

---

Status, adding, committing

```bash
mkdir Fractal; cd Fractal
git init
tree .git
cat .git/config
git status
cp ../versions/01/visualize.py .
pcat ../visualize.py
git status
git commit -m "Add visualization module"
git config --global user.email "student@example.com"
git config --global user.name "Git Learner"
git status
git commit -m "Add visualization module"
git status
cp ../versions/01/mandelbrot-1.py mandelbrot.py
cp ../versions/01/Mandelbrot.md .
git status
nano visualize.py
git add *
git status
git commit  # interactive edits
cp ../versions/01/mandelbrot-2.py mandelbrot.py 
git status
git add .
git commit -m "Add doctest to mandelbrot"
cp ../versions/01/mandelbrot-3.py mandelbrot.py 
git add mandelbrot.py
git diff
git commit -m "Enhance doctests"
git diff
git log
```

---

Version history, branches

```bash
git config --add --global core.pager less
cat ~/.gitconfig 
git log
git checkout 1681b88692e269f130f4b3f8dd922789be163083
git branch
git branch use-directories
git branch
git checkout use-directories
git rm *
cp -rv ../versions/02/* .
git status
git add -Av
git status  # Note files renamed
git commit -m "Refactor to directory structure"
git status
tree
pcat fractal/visualize.py | less -r
touch README 
touch LICENSE
git add README LICENSE
git commit -m "Placeholder README and LICENSE"
git log
git branch integrate-tests
git branch
git checkout integrate-tests
git branch
rm -rf fractal test
cp -rv ../versions/03/* .
nano README
git diff
git status
git add .   
git status    # Note rename, delete
git commit -m "Unify tests"
tree
git checkout master
tree
git branch
git checkout integrate-tests
tree
# This is very optional, but useful
gb() { git branch --show-current 2>/dev/null; }
export PS1='\e[0;35m\W\e[0m|\e[0;32m$(gb)\e[0m $ '
git log
git checkout master
git log
git checkout -B divergent-test
git log
echo "Divergence is confusing" > README
git add README
git commit -m "Divergent README"
tree
git checkout integrate-tests
git log
cat README
git log --graph --all
git log --graph --oneline --all
git branch -D divergent-test
```

---

Merging, diffing

```bash
git checkout -B use-pytest master
ls
git rm *.py *.md
cp -rv ../versions/04/* .
git add .
git status
git commit -m "Pytest based test suite"

git checkout -B optimizations master
git rm *.py *.md
cp -rv ../versions/05/* .
git add .
git commit -m "Experiment with optimizations"

nano fractal/julia.py fractal/mandelbrot.py 
# Add numba to mandelbrot
git add fractal/mandelbrot.py 
git commit -m "Accelerate mandelbrot"
touch test/test_speed.py
git add test/*
git status
git commit -m "Verify speed"

git checkout use-pytest
touch test/test_speed.py
git status
git commit -m "Verify speed"

git log --graph --oneline --all
git diff aa4e070 a9c1816
git merge aa4e070 a9c1816
# trivial differences: trailing newline, obj id
nano fractal/mandelbrot.py test_failure.out 
git status
git add fractal/mandelbrot.py test_failure.out
git commit # interactive
git log --graph --oneline --all
```