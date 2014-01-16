import os
from bottle import route, run, request, response, redirect

@route('/', method='GET')
def get_index():
	return 'Hello world.'

if __name__ == '__main__':
	run(port=(os.environ.get('PORT') or 8787))
