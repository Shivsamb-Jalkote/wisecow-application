from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route("/")
def cow_art():
    quote = "Living your life is a task so difficult, it has never been attempted before."
    result = subprocess.run(["/usr/games/cowsay", quote], capture_output=True, text=True)
    return Response(f"<pre>{result.stdout}</pre>", mimetype='text/html')

# ✅ Add this so Flask starts the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
