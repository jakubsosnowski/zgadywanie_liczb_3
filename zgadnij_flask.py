from flask import Flask, request

app = Flask(__name__)

html_page_1 = """
    <html>
        <head>
            <title>Guess the Number</title>
        </head>
        <body>
            <h1>Please imagine number from 0 to 1000</h1>
            <form action="" method="POST">
                <input type ="hidden" name="min" value="{}"></input>
                <input type ="hidden" name="max" value="{}"></input>
                <input type ="submit" value="Try!">
            </form>
        </body>
    </html>
"""

html_main = """
    <html>
        <head>
            <title>Guess the Number</title>
        </head>
        <body>
            <h1>It is: {guess}</h1>
            <form action="" method="POST">
                <input type="submit" name="user_answer" value="too big">
                <input type="submit" name="user_answer" value="too small">
                <input type="submit" name="user_answer" value="you won">
                <input type="hidden" name="min" value="{min}">
                <input type="hidden" name="max" value="{max}">
                <input type="hidden" name="guess" value="{guess}">
            </form>
        </body>
    </html>
"""

html_win = """
    <html>
        <head>
            <title>Guess the number</title>
        </head>
        <body>
            <h1>I guess the number {guess}!</h1>
        </body>
    </html>
"""


@app.route("/",  methods=['GET', 'POST'])
def guess_the_number():
    if request.method == "GET":
        return html_page_1.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return html_win.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return html_main.format(guess=guess, min=min_number, max=max_number)
