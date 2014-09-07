UnitTesting-example
===================
Linux & OSX | Windows
------------|------------
 [![Build Status](http://img.shields.io/travis/randy3k/UnitTesting-example/master.svg)](https://travis-ci.org/randy3k/UnitTesting-example) | [![Build status](http://img.shields.io/appveyor/ci/randy3k/UnitTesting-example/branch/master.svg)](https://ci.appveyor.com/project/randy3k/UnitTesting-example/branch/master)

This is an getting start example on using [UnitTesting](https://github.com/randy3k/UnitTesting) to test a sublime 2 and 3 package locally and via CI services such as [travis-ci](https://travis-ci.org) and [appveyor](http://www.appveyor.com).

If you like it, you could send me some tips via [![](http://img.shields.io/gittip/randy3k.svg)](https://www.gittip.com/randy3k).

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

### Local machine

If the tests are written correctly and UnitTesting is installed, UnitTesting can be triggered via the command palette. Then in the input panel type your package name, in our case, `UnitTesting-example`. To run only tests in particular files, use `UnitTesting-example/foorbar.py`. `foobar.py` is a unix shell wildcard to match the file names, `UnitTesting-example/test*.py` is used in default.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/cp.png' width='500'></img>

The test results will be shown in the outout panel.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/op.png' width='500'></img>

- Asynchronized tests (ST 3 only)

Tests are run in the main thread and blocking the UI. Asychronized testing could be invoked via `UnitTesting (Async)` command. Async tests are usually slower than the sync tests because the UI takes time to repond. It is useful when there are non-blocking codes in the tests. Now, only local machine supports async tests, travis support is in the plan.

- Deferred tests (ST 3 only)

Tests can be written using the [deferred testcase](https://bitbucket.org/klorenz/sublimepluginunittestharness). Details will be released soon.

### Travis

If the tests can be run locally, let's put them to travis-ci and let travis-ci takes care of them. First, you have to copy a important file: [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) (caution: with a beginning dot) to your repo. Then change the env variable `PACKAGE` in [.travis.yml](https://github.com/randy3k/UnitTesting-example/blob/master/.travis.yml) to the name of your package.

Don't forget to login [travis-ci](https://travis-ci.org) and enable travis-ci for your repo. 
Finally, push to github and wait..


### Travis mutiple os support

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/mos.png' width='500'></img>

To enable [multiple os feature](http://blog.travis-ci.com/2014-05-13-multi-os-feature-available/) for travis-ci, you have to send an email to _support@travis-ci.com_. Muitiple os feature is under beta testing and is only enabled upon request (see the link for details).

### Appveyor

To enable Appveyor for windows platform tests, copy the file `appveyor.yml` to your repo, change the `PACKAGE` variable in [appveyor.yml](https://github.com/randy3k/UnitTesting-example/blob/master/appveyor.yml). The last but not least, login [appveyor](http://www.appveyor.com) to add your repo as a project.


### Build status badges
The following markdown is used to show the build status badges. I am using images from [shields.io](http:/shields.io) to provide consistent badges. Change the username and repo name accordingly.
```
Linux & OSX | Windows
------------|------------
 [![Build Status](http://img.shields.io/travis/randy3k/UnitTesting-example/master.svg)](https://travis-ci.org/randy3k/UnitTesting-example) | [![Build status](http://img.shields.io/appveyor/ci/randy3k/UnitTesting-example/branch/master.svg)](https://ci.appveyor.com/project/randy3k/UnitTesting-example/branch/master)
```


### Vagrant

Debugging in travis-ci could be difficult. To mock the travis-ci environment in your computer, you can use [vagrant](http://www.vagrantup.com). For most users, this section could be ignored.


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

