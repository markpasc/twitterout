# tumblrout #

`tumblrout` is a command line tool for exporting a Tumblr blog to local files.


## Installation ##

Install its dependencies from the `requirements.txt` file:

    $ pip install -r requirements.txt

Then you can install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

First, you'll need a Tumblr API key. Register an application on [the Applications page of tumblr.com](http://www.tumblr.com/oauth/apps) to get a key. Once you have a key, run the `configure` command:

    $ tumblrout configure
    OAuth Consumer Key: 68-A
    Secret Key: f73D85A83def7BC29580FEB9f087A69Bc6bfacd1DDDBEBfb2bAF52c1

    OAuth Verifier: 13b24c7D485A9C4e99F1B4b163ddAE6eE4b9917e
    Configured!

After entering your secret key, the authorization page should open in your web browser. After approving your app, copy the `oauth_verifier` from the URL of the resulting page and paste it at the `OAuth Verifier:` prompt.


## Usage ##

See `tumblrout --help` for supported commands.

    $ tumblrout -v verify
    INFO: Set log level to INFO
    INFO: Verified!

    $
