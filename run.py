from flasktutorial import create_app

app = create_app()

""" run without setting flask variables """
if __name__ == '__main__':
    app.run(debug=True)