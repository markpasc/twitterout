# twitterout #

`twitterout` is a command line tool for exporting a Twitter to local files.


## Installation ##

Install `twitterout` as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

First, you'll need a Twitter API access token. Register an application on [the Applications page of dev.twitter.com](https://dev.twitter.com/apps), then click the "Create my access token" button to get an access token. Once you have it, run the `configure` command:

    $ twitterout configure
    Consumer key: 3sJE5btgFco5kh4HGR1b
    Consumer secret: TfuunBJjZNo3phB47p7an0n53M40e6eGq18821u
    Access token: xta5ADPa4KtRnNdN8rylSsCHRu6C7xdSJMYawUSrH3rEKjT
    Access token secret: GYf3dlAGVZmqkdlGF7VWk0AgwJR1UOtJwKRuG3mO2

    Configured!

Boom, solutionized.


## Usage ##

See `twitterout --help` for supported commands.

    $ twitterout -v verify
    INFO: Set log level to INFO
    INFO: Verified!

    $ twitterout -v -v -v favorites out/
    INFO: Set log level to DEBUG
    DEBUG: Successful request through 237609354176643073 leaves 13 requests until 1348187624
    DEBUG: Successful request through 226428073241874432 leaves 12 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 216747232546914305 leaves 11 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 208679504158261248 leaves 10 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 197361705746051074 leaves 9 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 183315456348786688 leaves 8 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 173472857672781824 leaves 7 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 159416797001560064 leaves 6 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 143942646841356288 leaves 5 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 127137492133613568 leaves 4 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 106078929223299072 leaves 3 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 84663133402173440 leaves 2 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 58085929910419456 leaves 1 requests until 1348187624
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 28431044533 leaves 0 requests until 1348187624
    WARNING: Rate limited; trying again in 584 seconds
    WARNING: Over capacity; trying again in 10 seconds
    DEBUG: Successful request through 791491038 leaves 14 requests until 1348188532
    DEBUG: Successful request through 376054532 leaves 13 requests until 1348188532
    INFO: Saved all tweets!

    $
