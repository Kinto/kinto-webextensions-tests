# Kinto Webextensions Tests

This repo contains tests used by Firefox Test Engineering for verifying the Kinto stack being used to power [Mozilla's Web Extensions](https://wiki.mozilla.org/WebExtensions)
system. 

## General Configuration

* Python 3.6.0
* [Tox](https://tox.readthedocs.io/en/latest/)

## Running Tests

To run the test suite, do the following:

* set an environment variable called TEST_ENV to be one of `stage` or `prod`
* Run the tests using the command `tox`
