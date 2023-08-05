import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import predict_house_price

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("House Price Prediction"),
    dcc.Input(id="input-size", type="number", placeholder="Enter house size"),
    html.Div(id="output-price")
])

@app.callback(
    Output("output-price", "children"),
    [Input("input-size", "value")]
)
def update_output(input_value):
    if input_value is not None:
        predicted_price = predict_house_price(input_value)
        return f"Predicted price: ${predicted_price:,.2f}"
    else:
        return ""

if __name__ == "__main__":
    app.run_server(debug=True)
