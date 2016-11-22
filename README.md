This library provides python Flask utilities and static assets for rendering
OOJS-UI.

# Example

```python
from flask import Flask, render_template

from flask_oojsui import build_static_blueprint

app = Flask(__name__)


@app.route('/')
def root():
    # This template uses assets from OOJS-UI
    return render_template("index.html")

# Adds static assets for OOJS-UI to path
app.register_blueprint(build_static_blueprint("oojsui", __name__))

app.run(port=8080, debug=True)
```
