from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    content = """
    <h1>Welcome to My Flask Web Page</h1>
    <p>This is a very simple introduction to my web page, served by Flask in Docker.</p>

    <h2>BUT WHY?</h2>
    <ul>
        <li>I created this to explore self-hosting a website</li>
        <li>I also wanted to learn how to use it with Docker.</li>
        <li>Built this website in a NixOS environment for easy maintenance and propagation across different nodes later on.</li>
    </ul>

    <h3>Glad you're here. Enjoy exploring!</h3>
    <h4>Maybe I'll put up some advertisements... Hmm...</h4>
    """
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
