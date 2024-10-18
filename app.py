from flask import Flask, Markup

app = Flask(__name__)

@app.route("/")
def hello():
    content = """
    # Welcome to My Flask Web Page

    This is a very simple introduction to my web page, served by Flask in Docker.

    ## BUT WHY?
    - I created this to explore a self-hosting a website
    - I also wanted to learn how to use with Docker. 
    - Built this website in a NixOS environment for easy maintenance and propogation across different nodes later on.

    ### Glad you're here. Enjoy exploring!
    #### Maybe i'll put up some advertisements... Hmm...
    """
    return Markup(content.replace("\n", "<br>"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
