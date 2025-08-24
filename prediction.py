import pandas as pd
from prophet import Prophet

def predict_future(data, category=None, days=5):
    """
    Predict future expenses using Prophet.

    :param data: DataFrame with columns ['Date', 'Amount', 'Category']
    :param category: Optional, predict for a specific category
    :param days: Number of days to forecast
    :return: Average predicted expense for next `days`
    """

    if data.empty:
        return 0

    # Standardize column names
    df = data.rename(columns=str.lower)
    df = df.rename(columns={"date": "ds", "amount": "y", "category": "category"})

    # Filter by category if provided
    if category:
        df = df[df["category"] == category]
        if df.empty:
            return 0

    # Ensure datetime format
    df["ds"] = pd.to_datetime(df["ds"])

    # Initialize Prophet
    model = Prophet(daily_seasonality=True)
    model.fit(df[["ds", "y"]])

    # Create future dataframe
    future = model.make_future_dataframe(periods=days)

    # Predict
    forecast = model.predict(future)

    # Take only the next `days` predictions
    future_preds = forecast.tail(days)["yhat"]

    # Return average
    return future_preds.mean()


def predict_future_all(data, days=5):
    """
    Predict future expenses for all categories.

    :param data: DataFrame with columns ['Date', 'Amount', 'Category']
    :param days: Number of days to forecast
    :return: Dictionary with category as key and average predicted expense as value
    """
    if data.empty:
        return {}

    categories = data["Category"].unique()
    predictions = {}

    for cat in categories:
        predictions[cat] = predict_future(data, category=cat, days=days)

    return predictions
