UnitTesting-example
===================
[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.png?branch=master)](https://travis-ci.org/randy3k/UnitTesting-example)

This is an getting start example on using [UnitTesting](https://github.com/randy3k/UnitTesting) to test a sublime 2 and 3 package locally and via [travis-ci](https://travis-ci.org).

Preparation
---
1. Before to test anything, you have to install [UnitTesting](https://github.com/randy3k/UnitTesting) via Package Control or clone it from [source](https://github.com/randy3k/UnitTesting).
2. You also have to know how to write unittest testcases. Make sure you read the correct correspondence. ST2 developers should read [this](http://docs.python.org/2.6/library/unittest.html) and ST3 developers should read [this](http://docs.python.org/3.3/library/unittest.html). This is specially important if your sublime package supports both ST2 and ST3. You may also want to look that the files [\_\_init\_\_.py](https://github.com/randy3k/UnitTesting-example/blob/master/tests/__init__.py) abandd [test_hw.py](https://github.com/randy3k/UnitTesting-example/blob/master/tests/test_hw.py) under the `tests` directory for the minimal example.

3. Your package! In our case, it is [helloworld.py](https://github.com/randy3k/UnitTesting-example/blob/master/helloworld.py)


Note: in the moment of writing this document, it is not yet available in Package Control.




Locally
----
If you tests are written correctly and UnitTesting is installed, you can trigger UnitTesting via the command palette.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/cp.png' width='500'></img>

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/op.png' width='500'></img>

Travis
---
If you tests can be run locally, it's time to put them to travis-ci and let travis-ci takes care about the tests. There are two important files, [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) and [travis.sh](https://github.com/randy3k/UnitTesting-example/blob/master/travis.sh), which you need to copy to your package. You will have to edit [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) and change the env variable `PACKAGE` to the name of your package.

Then you need to login to [travis-ci](https://travis-ci.org) to enable travis-ci for your repo. 

Vagrant
---
Debugging in travis-ci could be difficult. To mock the travis-ci environment in your computer, you can use [vagrant](http://www.vagrantup.com). 


```
# clone the example (not necessary in your sublime packages directory)
git clone https://github.com/randy3k/UnitTesting-example
cd UnitTesting-example
# you can also launch `st2`
vagrant up st3 --provision
vagrant ssh st3
# if st2, change to sublime-text-2
python ~/.config/sublime-text-3/Packages/UnitTesting/sbin/run_scheduler.py UnitTesting-example
# after done, kill sublime
killall sublime_text
```
