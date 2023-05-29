from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = "Hello World!"
		return (data)


if __name__ == '__main__':
	app.run(debug=True)
