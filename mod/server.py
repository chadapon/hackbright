from flask import Flask, request
from random import choice, randint


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    """Say hello"""

    return '''
    <html>
        <body>
            <h1><a href='/' >Say Hello</a></h1>
        </body>
    </html>
    '''

@app.route('/lucky')
def lucky_number():
    """Provides a random lucky number"""
    # add code here of getting a lucky number and return a string
    # with the lucky number
    lucky_number = randint(1,10)
    print lucky_number
    lucky_message = "Your lucky number is %s" % lucky_number
    print lucky_message


    return "<html><body><h1>" + lucky_message + "</h1></body></html>"


    # '''
    # <html>
    #     <style>
    #     a {
    #     color:green;
    #     }
    #     p {
    #     color:pink;
    #     }
    #     </style>
    #     <body>
    #         <h1><a href='/' >Luck number</a></h1>
    #         <p>Test</p>
    #     </body>
    # </html>
    # '''


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
