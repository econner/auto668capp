Automating 668 Capp
===================

Making 668 Capp sentient.

Setup
-----

Setup a new virtual env and activate it

    virtualenv auto668capp_env
    source auto668capp_env/bin/activate

# Jeremy recommends using virtualenvwrapper
# Nice for managing lots of virtualenvs
# mkvirtualenv capp
# workon capp

Install portaudio using homebrew

    brew install portaudio

Install other requirements

    pip install -r requirements.txt


Set environment variable for the 668 capp oauth app/tokens.

In .bashrc write

	export CAPP_KEY=XXXXX
	export CAPP_SECRET=YYYYY

	export CAPP_TOKEN=ZZZZZZ
	export CAPP_TOKEN_SECRET=AAAAAA


Wishlist / Ideas
----------------
- Tweet when dryer finishes.
- Tweet when door opened / closed or when buzzing someone in.
- Detect when trash needs to be taken out.
- Report whether dishes are dirty or clean?
- Track last time I was cleaned.
- Determine when I need more groceries.
