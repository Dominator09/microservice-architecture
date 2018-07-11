from flask_restful import reqparse


def getUserParser():
    parser = reqparse.RequestParser()
    parser.add_argument('email')
    return parser

def registerUser():
    parser = reqparse.RequestParser()
    parser.add_argument('email',required=True,help="Email is requirerd")
    parser.add_argument('password')
    parser.add_argument('first_name')
    parser.add_argument('last_name')
    parser.add_argument('phone_no')
    parser.add_argument('country_code')
    
    return parser

def login():
    parser = reqparse.RequestParser()
    parser.add_argument('email',required=True,help="Email is required")
    parser.add_argument('password')
    return parser 

def forgotPassword():
    parser = reqparse.RequestParser()
    parser.add_argument('mobile',required=True,help="Mobile is required")
    return parser

def createStorage():
    parser = reqparse.RequestParser()
    parser.add_argument('size',required=True,help="provide size of disk")
    parser.add_argument('name',required=True, help="provide name of drive")
    parser.add_argument('access_token',required=True)
    return parser
