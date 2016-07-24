UnitTesting-example
===================

[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.svg?branch=master)](https://travis-ci.org/randy3k/UnitTesting-example) 
[![Build status](https://ci.appveyor.com/api/projects/status/9nnjlnj6tetbxuqd/branch/master?svg=true)](https://ci.appveyor.com/project/randy3k/unittesting-example/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/randy3k/UnitTesting-example/badge.svg?branch=master)](https://coveralls.io/github/randy3k/UnitTesting-example?branch=coverage)
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=Randy%2ecs%2elai%40gmail%2ecom&amp;lc=US&amp;item_name=Package&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3apaypal%2ddonate%2dyellow%2esvg%3aNonHosted" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" /></a>
<a href="https://gratipay.com/~randy3k/" title="Donate to this project using Gratipay"><img src="https://img.shields.io/badge/gratipay-donate-yellow.svg" /></a>


------------

This is an getting start example on using [UnitTesting](https://github.com/randy3k/UnitTesting) to test a sublime 2 and 3 package locally and via CI services such as [travis-ci](https://travis-ci.org) and [appveyor](http://www.appveyor.com).

For testing syntax_test files, go directly to [testing syntax_test files](README.md#testing-syntax_test-files).

Install [PackageReloader](https://github.com/randy3k/PackageReloader) to reload the package automatically before running the tests.


Preparation
---
1. Before testing anything, you have to install [UnitTesting](https://github.com/randy3k/UnitTesting) via Package Control or clone it from [source](https://github.com/randy3k/UnitTesting).
2. Your package! In our case, it is [helloworld.py](helloworld.py)
3. You also have to know how to write unittest testcases. TestCases should be placed in `test*.py` under the directory `tests` (configurable, see below). They are loaded by a modified [TestLoader](https://github.com/randy3k/UnitTesting/blob/master/unittesting/core/loader.py).
    - ST2 developers should read [this](http://docs.python.org/2.6/library/unittest.html) for unittest documentation.
    - ST3 developers should read [this](http://docs.python.org/3.3/library/unittest.html). 
    - You may also want to look that the file [test.py](tests/test.py) under the `tests` directory for the minimal example.



Running Tests
----

### Local machine

If the tests are written correctly and UnitTesting is installed, UnitTesting
can be triggered via the command palette. Then in the input panel type your
package name, in our case, `UnitTesting-example`. To run only tests in
particular files, enter `<Package name>:<filename>`. `<filename>` should be a
unix shell wildcard to match the file names, `<Package name>:test*.py` is used
in default.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/cp.png' width='500'></img>

The test results will be shown in the outout panel.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/op.png' width='500'></img>

There are also quick commands to run tests of the current project or file. If
[PackageReloader](https://github.com/randy3k/PackageReloader) is installed,
you could run the command `UnitTesting: Reload ....` to reload and run the
current tests.

Besides the test results, UnitTesting also provides commands to check test coverage
via [coverage](https://pypi.python.org/pypi/coverage).
<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/coverage.png' width='500'></img>


### Travis and Appveyor

If the tests can be run locally, let's put them to travis-ci and let travis-ci
takes care of them. First, you have to copy a important file:
[.travis.yml](.travis.yml) (caution: with a beginning dot) to your repo. Then
change the env variable `PACKAGE` in [.travis.yml](.travis.yml) to the name of
your package. Don't forget to login [travis-ci](https://travis-ci.org) and
enable travis-ci for your repo. Finally, push to github and wait..

To enable Appveyor for windows platform tests, copy the file `appveyor.yml` to
your repo, change the `PACKAGE` variable in [appveyor.yml](appveyor.yml). The
last but not least, login [appveyor](http://www.appveyor.com) to add your repo
as a project.

Installation of Sublime Text on Travis and Appveyor are handled by the scripts
in [sublime-text-
installer](https://github.com/randy3k/sublime_text_installer).

### Installing Package Control

If your package uses Package Control dependencies, you may want to install
Package Control by umcommenting the line of `install_package_control` in
[.travis.yml](.travis.yml) or [appveyor.yml](appveyor.yml).


### Testing syntax_test files on CIs

To enable testing of the syntax_test files, please copy the
[.travis.yml](.travis.yml) or [appveyor.yml](appveyor.yml), and use the
`run_syntax_tests` in those files. Check [syntax](https://github.com/randy3k
/UnitTesting-example/tree/syntax) branch for an example.


Coverage and Coveralls.io
---

To generate coverage report via [coveralls.io](https://coveralls.io/), you
just have to specific three things in `.travis.yml`

1. install [python-coveralls](https://pypi.python.org/pypi/python-coveralls/)
1. run the test will the `--coverage` flag
    ```
    sh travis.sh run_tests --coverage
    ```

1. run `coveralls` after success

Check [.travis.yml](.travis.yml) for details. The file
[.coveragerc](.coveragerc) is used to control the coverage configuations. If
it is missing, UnitTesting would still ignore the `tests` directory.


Options
----

### Use a different test directory

The default test directory is "tests". To change the test directory, add a
file `unittesting.json` to your repo with the corresponding directory name, eg
`unittest`:

```
{
    "tests_dir" : "unittest"
}
```

### Redirect test result to a file

The test result could be redirected to a file by specifying the `output`
variable in `unittesting.json`. It can also be redirected to a temporary file
by using `"output": "<tempfile>"`. The temporary file will be opened in the
current window.

```
{
    "output" : "foo.txt"
}
```

### Deferred testing
Tests can also be written using the [deferrable testcase](https://bitbucket.org/klorenz/sublimepluginunittestharness).

It provides deferred testcases, such you are able to run sublime commands from
your test cases and give control to sublime text and get it back later. Would
be useful to test `sublime_plugin.EventListener`.

A example would be found in [deferred](https://github.com/randy3k/UnitTesting-example/tree/deferred) branch.

To activate deferred testing on travis and appveyor. Add the file
`unittesting.json` to your repo with the following:

```
{
    "deferred": true,
}
```

### Async testing (ST 3 only)

Tests are running in the main thread and blocking the UI. Asychronized testing
could be used if you need the UI to respond. Async tests are usually slower
than the sync tests because the UI takes time to repond. It is useful when
there are non-blocking codes in the tests. A example would be found in
[async](https://github.com/randy3k/UnitTesting-example/tree/async) branch.

To activate async testing on travis and appveyor. Add the file
`unittesting.json` to your repo with the following:

```
{
    "async": true,
}
```

Note: 

1. `async` is forced to be `false` on ST2
2. if `async` is true, `deferred` is forced to be `false`.


### Troubleshooting

If you keep encountering unexpected errors, you may want to check the
`close_windows_when_empty` setting. I have spent at least a few hours to
realize this was the cause of a error. The `true` value would close the last
window if there is no view. It is fine if you are running blocking code.
However, if you are using deferred or async testcases, this is something you
definitely want to check.


### Vagrant

Debugging in travis-ci could be difficult. To mock the travis-ci environment
in your computer, you can use [vagrant](http://www.vagrantup.com). For most
users, this section could be ignored.


```
# clone the example to somewhere
git clone https://github.com/randy3k/UnitTesting-example
cd UnitTesting-example
# you can also launch `st2` config
vagrant up st3
# enter ssh
vagrant ssh st3
# run tests
sh vagrant.sh run_tests
```
