# UnitTesting-example

[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.svg?branch=master)](https://travis-ci.org/randy3k/UnitTesting-example) 
[![Build status](https://ci.appveyor.com/api/projects/status/9nnjlnj6tetbxuqd/branch/master?svg=true)](https://ci.appveyor.com/project/randy3k/unittesting-example/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/randy3k/UnitTesting-example/badge.svg?branch=master)](https://coveralls.io/github/randy3k/UnitTesting-example?branch=coverage)
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=Randy%2ecs%2elai%40gmail%2ecom&amp;lc=US&amp;item_name=Package&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3apaypal%2ddonate%2dyellow%2esvg%3aNonHosted" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg" /></a>
<a href="https://gratipay.com/~randy3k/" title="Donate to this project using Gratipay"><img src="https://img.shields.io/badge/gratipay-donate-yellow.svg" /></a>


------------

This is an simple example to use
[UnitTesting](https://github.com/randy3k/UnitTesting) to test a Sublime Text
package on a local machine and via continuous integration services such as
[travis-ci](https://travis-ci.org) and [appveyor](http://www.appveyor.com).

For testing syntax_test files, go directly to [testing syntax_test files](README.md#testing-syntax_test-files-on-cis).


## Preparation

1. Before testing anything, you have to install [UnitTesting](https://github.com/randy3k/UnitTesting) via Package Control.
2. Your package! In our case, it is [helloworld.py](helloworld.py)
3. TestCases should be placed in `test*.py` under the directory `tests` (configurable, see below). They are loaded by a modified [TestLoader](https://github.com/randy3k/UnitTesting/blob/master/unittesting/core/loader.py), see [TestLoader.discover](https://docs.python.org/3.3/library/unittest.html#unittest.TestLoader.discover) for more details. (Sublime Text 2 developers should read [this](http://docs.python.org/2.6/library/unittest.html) for unittest documentation).
4. Take a look of the file [test.py](tests/test.py) under the `tests` directory for a minimal example.



## Running Tests

### Local machine

UnitTesting can be triggered via the command palette command `UnitTesting`.
Enter the package name in the input panel and hit enter, a console should pop
up and the tests should be running. To run only tests in particular files,
enter `<Package name>:<filename>`. `<filename>` should be a unix shell
wildcard to match the file names, `<Package name>:test*.py` is used in
default.


### Reload and coverage

If [PackageReloader](https://github.com/randy3k/PackageReloader) is installed,
you could run the command `UnitTesting: Reload and Test Current Project` to
reload and run the current project.

<img src='https://raw.github.com/randy3k/UnitTesting-example/fig/local.gif' width='600'></img>

Furthermore, it is also possible to check test
coverage via [coverage](https://pypi.python.org/pypi/coverage). The corresponding command is
`UnitTesting: Test Current Project with Coverage`.

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

### Coverage and Coveralls.io support on Travis.

*This feature is Sublime Text 3 only*

To generate coverage report for [coveralls.io](https://coveralls.io/), you
just have to specific three things in `.travis.yml`

1. run the test with the `--coverage` flag
    ```
    sh travis.sh run_tests --coverage
    ```

1. install [python-coveralls](https://pypi.python.org/pypi/python-coveralls/)
1. run `coveralls` after success

Check [.travis.yml](.travis.yml) for details. The file
[.coveragerc](.coveragerc) is used to control the coverage configuations. If
it is missing, UnitTesting will ignore the `tests` directory.

### Installing Package Control and Dependencies

If your package uses Package Control dependencies, you may want to install
Package Control by umcommenting the line of `install_package_control` in
[.travis.yml](.travis.yml) or [appveyor.yml](appveyor.yml).


### Testing syntax_test files

To enable testing of the syntax_test files, please copy the
[.travis.yml](.travis.yml) or [appveyor.yml](appveyor.yml), and use the
`run_syntax_tests` in those files. Check 
[syntax](https://github.com/randy3k/UnitTesting-example/tree/syntax) branch for an example.



## Options

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
variable in `unittesting.json`.

```
{
    "output" : "foo.txt"
}
```

### Deferred testing

Tests can also be written using the Deferrable testcase, such that you are
able to run sublime commands from your test cases and yield control to sublime
text runtime and continue the execution later. Would be useful to test
asynchronous codes.

A example would be found in [deferred](https://github.com/randy3k/UnitTesting-example/tree/deferred) branch.

To activate deferred testing on travis and appveyor. Add the file
`unittesting.json` to your repo with the following:

```
{
    "deferred": true,
}
```

### Async testing (Sublime Text 3)

In default, the tests are running in the main thread and can block the
graphic inference. Asychronized testing could be used if you need the
interface to respond. 

Async tests are usually slower than the sync tests because the interface takes
time to repond but it is useful when there are blocking codes in the tests. A
example would be found in 
[async](https://github.com/randy3k/UnitTesting-example/tree/async) branch. 

It is known that async test does not work very well with coverage, and
deferred testing usually performs better than async testing.


To activate async testing on travis and appveyor. Add the file
`unittesting.json` to your repo with the following:

```
{
    "async": true,
}
```

Note: 

1. `async` is forced to be `false` on Sublime Text 2
2. if `async` is true, `deferred` is forced to be `false` (relaxation of this is in progress)



## Vagrant (**Outdated**)


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
