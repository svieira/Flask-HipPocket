from flask import url_for


def mapper_index():
    return "Mapper Index Page"


def overridden_endpoint():
    return "The url for url_for('endpoint_name') is " + url_for("endpoint_name")


def post_only():
    return "Only accessible via POST"
