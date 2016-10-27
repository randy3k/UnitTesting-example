UnitTesting-example
===================
Linux & OSX | Windows
------------|------------
[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.svg?branch=async)](https://travis-ci.org/randy3k/UnitTesting-example) | [![Build status](https://ci.appveyor.com/api/projects/status/l8x5laog8rs2t4p6/branch/async?svg=true)](https://ci.appveyor.com/project/randy3k/unittesting-example/branch/async)

Example of a blocking testcase.

In [test.py](tests/test.py), `time.sleep(1)` will block Sublime Text and `async_insert_hello_world` wouldn't have a chance to be execulated before the line of assertion. Therefore, the option of `async` will be necessary.
