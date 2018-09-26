from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

#Comment out the localhost part, to test Apache configuration. 
#run(host='localhost', port=8080, debug=True)