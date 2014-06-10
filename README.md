UnitTesting-example
===================
[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.png?branch=master)](https://travis-ci.org/randy3k/UnitTesting-example)

This is an getting start example on using [UnitTesting](https://github.com/randy3k/UnitTesting) to test a sublime 2 and 3 package locally and via [travis-ci](https://travis-ci.org).

Preparation
---
1. Before testing anything, you have to install [UnitTesting](https://github.com/randy3k/UnitTesting) via Package Control or clone it from [source](https://github.com/randy3k/UnitTesting).
2. Your package! In our case, it is [helloworld.py](https://github.com/randy3k/UnitTesting-example/blob/master/helloworld.py)
3. You also have to know how to write unittest testcases. TestCases should be placed in `test*.py` under the directory `tests`. They are loaded by a modified [TestLoader](https://github.com/randy3k/UnitTesting/blob/master/loader.py).
    - ST2 developers should read [this](http://docs.python.org/2.6/library/unittest.html) for unittest documentation.
    - ST3 developers should read [this](http://docs.python.org/3.3/library/unittest.html). 
    - You may also want to look that the file [test.py](https://github.com/randy3k/UnitTesting-example/blob/master/tests/test.py) under the `tests` directory for the minimal example.

------------

Running Tests
----

###Locally

If the tests are written correctly and UnitTesting is installed, UnitTesting can be triggered via the command palette.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/cp.png' width='500'></img>

Then in the input panel type your package name, in our case, `UnitTesting-example`.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/op.png' width='500'></img>

###Travis

If the tests can be run locally, let's put them to travis-ci and let travis-ci takes care of them. First, you have to copy a important file: [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) (caution: with a beginning dot) to your repo. Then change the env variable `PACKAGE` in [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) to the name of your package.

Don't forget to login [travis-ci](https://travis-ci.org) and enable travis-ci for your repo. 
Finally, push to github and wait..

###Vagrant

Debugging in travis-ci could be difficult. To mock the travis-ci environment in your computer, you can use [vagrant](http://www.vagrantup.com). You can ignore this section if your travis-ci builds are good.


```
# clone the example (not necessary in your sublime packages directory)
git clone https://github.com/randy3k/UnitTesting-example
cd UnitTesting-example
# you can also launch `st2`
vagrant up st3 --provision
vagrant ssh st3
# if st2, change to sublime-text-2
python ~/.config/sublime-text-3/Packages/UnitTesting/sbin/run.py UnitTesting-example
# after done, kill sublime
killall sublime_text
```
