from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


@app.route("/")  # define home page
def home():
    return render_template("home.html")


prediction_request_parser = reqparse.RequestParser(bundle_errors=True)
prediction_request_parser.add_argument(
    "arg_1", type=float, help='arg_1 is required', required=True)
prediction_request_parser.add_argument(
    "arg_2", type=float, help='arg_2 is required', required=True)
prediction_request_parser.add_argument(
    "arg_3", type=float, help='arg_3 is required', required=True)
prediction_request_parser.add_argument(
    "arg_4", type=float, help='arg_4 is required', required=True)


class predict(Resource):
    def post(self):
        # must be json serializable. Dict, list, tuples, int, strings and floats

        # returns something like dictionary
        args = prediction_request_parser.parse_args()

        return args, "201"


api.add_resource(predict, "/predict")


if __name__ == "__main__":
    app.run(debug=True)
