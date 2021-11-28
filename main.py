
from quart import Quart, make_push_promise, render_template, url_for

app = Quart(__name__)

@app.route('/')
async def index():
    await make_push_promise(url_for('static', filename='style.css'))
    return await render_template('index.html')

app.run()