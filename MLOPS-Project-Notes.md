
## Production Grade MLOps

- CI/CD: GitHub Actions
- CT/CD/CM: Airflow
- Model Registry: MLflow
- Deployment: AWS SageMaker


| Folder      | Purpose                                    |
| ----------- | ------------------------------------------ |
| `airflow/`  | Orchestration (CT, retraining, monitoring) |
| `mlflow/`   | Experiment tracking & model registry       |
| `app/`      | SageMaker inference container              |
| `training/` | Model training code                        |
| `scripts/`  | AWS automation                             |
| `.github/`  | CI/CD                                      |
| `config/`   | Environment configs                        |


Project Flow

GitHub Push
   ↓
GitHub Actions (CI)
   ↓
Airflow (Train → Evaluate → Register)
   ↓
MLflow
   ↓
SageMaker Deploy
   ↓
Monitoring DAG → Retrain DAG