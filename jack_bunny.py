from flask import request, Flask, render_template, redirect

app = Flask(__name__)


class Commands(object):
    def g(arg=None):
        """'g [insert query]' searching with ecosia"""
        if arg:
            return 'https://www.ecosia.org/search?q={0}&addon=opensearch'.format(arg)
        else:
            return 'https://www.ecosia.org'

    def rg(arg=None):
        """'rg/google [insert query]' searching with google"""
        if arg:
            return 'http://www.google.com/search?q={0}'.format(arg)
        else:
            return 'https://www.google.com'
    google = rg

    def cpp(arg=None):
        """'cpp [insert query]' searches for syntactical cpp terms on cppreference.com"""
        if arg:
            return 'http://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search={0}'.format(arg)
        else:
            return 'http://en.cppreference.com/w/'

    def yt(arg=None):
        """'yt [insert query]' make a youtube search. If not query is passed in, defaults to the youtube homepage"""
        if arg:
            return 'http://www.youtube.com/results?search_query={0}&search_type=&aq=-1&oq='.format(arg)
        else:
            return 'http://www.youtube.com'

    def d(arg=None):
        """'d [insert query]' make a google definition search. If not query is passed in, defaults to dictionary.com"""
        if arg:
            return 'https://www.google.com/search?q=define%3A+{0}'.format(arg)
        else:
            return 'http://www.dictionary.com/'

    def help(arg=None):
        """'help' returns a list of usable commands """
        help_list = set()
        for values in Commands.__dict__.values():
            if callable(values):
                help_list.add(values.__doc__)
        return help_list


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/q/')
def route():
    # process the query
    try:
        query = str(request.args.get('query', ''))
        tokenized_query = query.split(' ', 1)
        search_command = tokenized_query[0].lower()
        option_args = None
        if len(tokenized_query) == 2:
            option_args = tokenized_query[1]
    except Exception as e:
        print(e)
        search_command = query
        option_args = None

    try:
        command = getattr(Commands, search_command)
        if search_command == 'help':
            return render_template('help.html', command_list=command(None))
        url = command(option_args)
        return redirect(url)
    except Exception as e:
        # fallback option is to google search
        print(e)
        return redirect(Commands.g(query))


if __name__ == '__main__':
    app.run()
