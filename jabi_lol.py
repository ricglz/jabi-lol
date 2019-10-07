from flask import request, Flask, render_template, redirect
from commands import Commands

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/q/')
def route():
    # process the query
    try:
        query = str(request.args.get('query', ''))
        tokenized_query = query.split(' ', 1)
        if query == tokenized_query[0]:
            tokenized_query = query.split('/', 1)
        search_command = tokenized_query[0].lower()
        option_args = tokenized_query[1] if len(tokenized_query) == 2 else None
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
