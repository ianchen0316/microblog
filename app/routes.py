from app import application

@application.route('/')
@application.route('/index')
def index():

    # Mock data
    user = {'username' : 'Miguel'}

    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + ''' </h1>
        </body>
    </html>
    '''
