from flask import Flask
from graphql_server.flask import GraphQLView

import schema

import process

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True,
))

@app.route('/')
def hello():
    return "<h1>Hello, world!</h1>"




@app.route('/data')
def data():
    bookings = process.getBookings()
    output = ""
    for booking in bookings:
        output += ("<p>")
        output += (process.prettyPrint(booking))
        output += ("</p>")

    return output





if __name__ == "__main__":
    app.run(debug=True)