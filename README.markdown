# twitterout #

`twitterout` is a command line tool for exporting a Twitter to local files.


## Installation ##

Install its dependencies from the `requirements.txt` file:

    $ pip install -r requirements.txt

Then you can install it as any other Python program:

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

    $ tumblrout -v verify
    INFO: Set log level to INFO
    INFO: Verified!

    $
