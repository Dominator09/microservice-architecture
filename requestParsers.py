from flask_restful import reqparse


def getUserParser():
    parser = reqparse.RequestParser()
    parser.add_argument('email')
    return parser

def registerUser():
    parser = reqparse.RequestParser()
    parser.add_argument('email',required=True,help="Email is requirerd")
    parser.add_argument('password')
    return parser

def login():
    parser = reqparse.RequestParser()
    parser.add_argument('email',required=True,help="Email is requirerd")
    parser.add_argument('password')
    return parser            