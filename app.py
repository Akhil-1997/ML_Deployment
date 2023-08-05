import joblib

def predict_house_price(size):
    # Replace this with your actual trained machine learning model
    # For demonstration purposes, we'll use a dummy model that just multiplies the input size by 1000.
    predicted_price = size * 1000

    return predicted_price

if __name__ == "__main__":
    # You can include code to train your machine learning model here
    # For simplicity, we'll use a dummy model and save it using joblib
    from sklearn.linear_model import LinearRegression
    import numpy as np

    # Create dummy data for demonstration purposes
    np.random.seed(0)
    X_train = np.random.rand(100, 1) * 200
    y_train = X_train * 1000

    # Train the dummy model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model using joblib
    joblib.dump(model, "trained_model.pkl")
