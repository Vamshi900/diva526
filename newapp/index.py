# loading necessary modules
from dash import html, dcc
from dash.dependencies import Input, Output

# loading application component/webpages
from app_our import app,port
from screens.storyline import StoryLine
from screens.predictor import Predictor
# from screens.dashboard import Dashboard
from app import app


app.layout = html.Div([
    dcc.Location(id = 'url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'), 
    Input('url', 'pathname')
)
def visiting_page(path):
    if path == "/story":
        return StoryLine()
    elif  path=="/pred":
        return Predictor()
    else:
        return app()

if __name__ == "__main__":
    app.run_server("0.0.0.0",port=port, debug=False)