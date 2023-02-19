from flask import Flask
from flask_cors import CORS
from graphql_server.flask import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

import schema
import process
from queries import listBookings_resolver

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xwdkqoqi:u4JN-9OV9WA_X6SSkdMIP3AOr-m-wxOM@hansken.db.elephantsql.com/xwdkqoqi"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

query = ObjectType("Query")
query.set_field("listBookings", listBookings_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = process.toJson()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


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