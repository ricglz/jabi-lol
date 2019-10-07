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

    def i(arg=None):
        """'in [insert query]' searches for users or takes you to the home page"""
        if arg:
            return 'https://instagram.com/{0}'.format(arg)
        else:
            return 'https://instagram.com'
    def r(arg=None):
        """'r [insert query]' searches for subrredit"""
        if arg:
            return 'https://www.reddit.com/r/{0}/'.format(arg)
        else:
            return 'https://reddit.com'

    def help(arg=None):
        """'help' returns a list of usable commands """
        help_list = set()
        for values in Commands.__dict__.values():
            if callable(values):
                help_list.add(values.__doc__)
        return help_list
