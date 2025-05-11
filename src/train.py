import os
import mlflow
from sklearn.ensemble import RandomForestRegressor
from data.data_processor import DataProcessor
from models.model_trainer import ModelTrainer
from models.predictor import Predictor

def main():
    # Initialize components
    data_processor = DataProcessor()
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    trainer = ModelTrainer(model, experiment_name="mlops_project")
    
    # Load and preprocess data
    # Note: Replace with your actual data path
    data_path = "data/raw/dataset.csv"
    data = data_processor.load_data(data_path)
    X, y = data_processor.preprocess_data(data, target_column="target")
    
    # Train model
    train_metrics, test_metrics = trainer.train(X, y)
    print("Training metrics:", train_metrics)
    print("Testing metrics:", test_metrics)
    
    # Save the model
    model_path = "models/saved/model"
    trainer.save_model(model_path)
    
    # Test prediction
    predictor = Predictor(model_path)
    sample_prediction = predictor.predict(X[:1])
    print("Sample prediction:", sample_prediction)

if __name__ == "__main__":
    main() 