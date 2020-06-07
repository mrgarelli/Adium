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
- run function via - specifically function run_tests()
> python3 ublock_tests.py
- will return False if ads present, True if ads not present


# TODO:

* [ ] look into why 0 out of 0 ad filters used when loading
    * [ ] look into how uBlock loads extensions - what filters do they turn on/how? Do they pull in any other dependencies? If so, at what point/how?
* [ ] create new images in place of uBlock - Ben
* [ ] modify build scripts to identify mentions of uBlock and change them to Adium - Matt
    * [ ] run tests for any instances of words 'ublock' within code, fail if present
* [ ] setup django backend
* [ ] insert ad on page
* [ ] add cached build folder (for previous builds of uBlock)
* [ ] deploy to chrome store - Ben
* [x] test on mac
* [x] integrate ublock success tests (blocks ads)
* [x] improve integration tests (new sites - reddit, google page, etc) - Ben
* [x] programatically turn all 'off' settings to FALSE at this location: /Adium/uBlock/platform/chromium/assets/assets.json
