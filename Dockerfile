FROM python:3.10-slim
WORKDIR /app
RUN pip install flask scikit-learn==1.2.1 joblib "numpy<2.0.0"
COPY app.py .
COPY models/ models/
CMD ["python", "app.py"]