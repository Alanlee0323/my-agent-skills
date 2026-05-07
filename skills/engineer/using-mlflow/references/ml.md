# MLflow Practical Reference

Use this as the default reference for implementing MLflow in real projects.

## 1. Setup and First Run

### 1.1 Install
```bash
pip install mlflow
```

### 1.2 Local UI
```bash
mlflow ui --port 5000
```

Open `http://127.0.0.1:5000`.

### 1.3 Minimal tracking example
```python
import mlflow

mlflow.set_experiment("demo-exp")

with mlflow.start_run(run_name="baseline"):
    mlflow.log_param("model_type", "xgboost")
    mlflow.log_metric("rmse", 0.412)
    mlflow.log_artifact("reports/metrics.json")
```

## 2. Remote Tracking Server

### 2.1 Start server with DB backend and object storage
```bash
mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri postgresql://user:pass@db:5432/mlflow \
  --artifacts-destination s3://mlflow-artifacts
```

### 2.2 Point client to server
```python
import mlflow
mlflow.set_tracking_uri("http://mlflow.mycompany.internal:5000")
```

## 3. Artifact Store Notes
- Keep metadata in backend store (DB), artifacts in object storage.
- Configure cloud credentials on both server and clients if required by storage backend.
- For S3-compatible storage, endpoint and security env vars must be consistent.

Common environment variables:
```bash
export MLFLOW_S3_ENDPOINT_URL=https://s3.us-west-1.amazonaws.com
export MLFLOW_S3_EXPECTED_BUCKET_OWNER=123456789012
```

## 4. Model Logging and Registry

### 4.1 Log model to a run
```python
import mlflow
import mlflow.sklearn

with mlflow.start_run() as run:
    mlflow.sklearn.log_model(sk_model=model, artifact_path="model")
```

### 4.2 Register model version
```python
import mlflow

model_uri = f"runs:/{run.info.run_id}/model"
mlflow.register_model(model_uri=model_uri, name="fraud-detector")
```

### 4.3 Load by registry URI
```python
import mlflow.pyfunc

loaded = mlflow.pyfunc.load_model("models:/fraud-detector/1")
```

## 5. Common Team Patterns
- One experiment per feature/domain (`ranking-v2`, `fraud-detection`, etc.).
- Use consistent run tags (`team`, `dataset_version`, `git_commit`, `stage`).
- Log both primary and guardrail metrics.
- Store dataset or feature snapshot identifiers in params/tags for traceability.
- Keep artifact paths stable to simplify automation.

## 6. Troubleshooting

### 6.1 UI is empty
- Check `MLFLOW_TRACKING_URI`.
- Verify experiment name and active run creation.
- Verify client writes to the same server the UI reads from.

### 6.2 Artifact upload/download fails
- Verify storage credentials and region/endpoint settings.
- Check server-side artifact destination and network access.
- Validate that client and server can resolve the same artifact URI.

### 6.3 Registry operations fail
- Ensure server has model registry support enabled with DB backend.
- Verify permissions if auth is enabled.
- Confirm model URI exists and run artifacts are accessible.

### 6.4 Inconsistent experiment lineage
- Enforce run tags for `git_commit`, `data_version`, and `pipeline_id`.
- Add CI checks to block promotion if required tags are missing.

## 7. Official Links
- Docs home: https://mlflow.org/docs/latest/
- Tracking: https://mlflow.org/docs/latest/ml/tracking/
- Quickstart: https://mlflow.org/docs/latest/ml/tracking/quickstart/
- Tracking server architecture: https://mlflow.org/docs/latest/self-hosting/architecture/overview/
- Artifact stores: https://mlflow.org/docs/latest/self-hosting/architecture/artifact-store/
- Model Registry workflow: https://mlflow.org/docs/latest/ml/model-registry/workflow/
