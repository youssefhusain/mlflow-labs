
# Getting Started with MLflow

To track experiments using MLflow, follow the steps below:

## 1. Start the MLflow UI

Run the following command in your terminal:

```bash
python -m mlflow ui
```

This will launch the MLflow Tracking UI at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##  2. Main Code Components

### Set the MLflow tracking URI (Local):

```python
mlflow.set_tracking_uri("http://127.0.0.1:5000")
```

### Create a new experiment:

```python
experiment_id = mlflow.create_experiment(name="text 2")
```

### Start a run and log metrics and artifacts:

```python
mlflow.start_run(experiment_id=experiment_id, run_name="first run")

mlflow.log_metric("acc", 0.9)            # Log accuracy metric
mlflow.log_artifact("test.txt")         # Log a local file as an artifact
```

---

##  Change the username (Optional)

To change the logged username in MLflow, use:

```python
import os
os.environ["LOGNAME"] = "joe"
```

---

##  Notes

- Make sure the file `test.txt` exists in the current directory before logging it.
- Don’t forget to import required libraries at the top:

```python
import mlflow
import os
```
