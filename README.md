UnitTesting-example
===================
Linux & OSX | Windows
------------|------------
[![Build Status](https://travis-ci.org/randy3k/UnitTesting-example.svg?branch=deferred)](https://travis-ci.org/randy3k/UnitTesting-example) | [![Build status](https://ci.appveyor.com/api/projects/status/l8x5laog8rs2t4p6/branch/deferred?svg=true)](https://ci.appveyor.com/project/randy3k/unittesting-example/branch/deferred)

Example of a deferrable testcase.

## Some details about DeferrableTestCase

[DeferrableTestCase][1] is used to write the test cases. They are executed by
the [DeferringTextTestRunner][2] and the runner expects not only regular test
functions, but also generators. If the test function is a generator, it does
the following

- if the yielded object is a callable, the runner will evaluate the
  [callable][3] and check its returned value. If the result is `True`, the
  runner continues the generator, if not, the runner will wait until the
  condition is met.

- If the yielded object is an integer, say `x`, then it will [continue][4] the
  generator after `x` ms.

- Otherwise, the `yield` statement will always wait for 10 ms.
  
[1]: https://github.com/randy3k/UnitTesting/blob/dc810ee334bb031710b859478faaf50293880995/unittesting/core/st3/runner.py#L49
[2]: https://github.com/randy3k/UnitTesting/blob/dc810ee334bb031710b859478faaf50293880995/unittesting/core/st3/runner.py#L7
[3]: https://github.com/randy3k/UnitTesting/blob/dc810ee334bb031710b859478faaf50293880995/unittesting/core/st3/runner.py#L49
[4]: https://github.com/randy3k/UnitTesting/blob/dc810ee334bb031710b859478faaf50293880995/unittesting/core/st3/runner.py#L57
