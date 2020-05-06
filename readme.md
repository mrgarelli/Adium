> ./ops

# Installation

* create and activate virtualenv using xonsh
```
xontrib vox
virtualenv env
vox activate env
```

* install all dependencies
```
pip install -i https://test.pypi.org/simple/ syspy
pip install -i https://test.pypi.org/simple/ declarecli
pip install -r requirements.txt
```

* deactivate virtualenv
```
vox deactivate
```

# Testing

ublock browser tests:
- files under tests/ublock_tests
- run function via - specificaly function run_tests()
> python3 ublock_tests.py
- will return False if ads present, True if ads not present


# TODO:

* [ ] change all mentions of uBlock/uBlock origin to Adium - Matt
* [ ] create new images in place of uBlock - Ben
* [ ] modify build scripts to identify mentions of uBlock and change them to Adium - Matt
* [ ] run tests for any instances of words 'ublock' within code, fail if present
* [ ] integrate ublock success tests (blocks ads)
* [x] improve integration tests (new sites - reddit, google page, etc) - Ben
* [ ] add cached build folder (for previous builds of uBlock)
* [ ] deploy to chrome store - Ben
* [ ] test on mac
* [ ] get Ben set up with Ubuntu (if test works on mac)
