# Innovate Analytics MLOps Project

## Project Overview
This repository contains the end-to-end MLOps implementation for Innovate Analytics Inc.'s machine learning system. The project demonstrates best practices in MLOps, including automated pipelines, version control, containerization, and deployment.

## Project Structure
```
.
├── .github/                    # GitHub Actions workflows
├── airflow/                    # Airflow DAGs and configurations
├── data/                      # Data storage (gitignored)
│   ├── raw/                   # Raw data
│   ├── processed/             # Processed data
│   └── models/                # Trained models
├── notebooks/                 # Jupyter notebooks for exploration
├── src/                       # Source code
│   ├── data/                  # Data processing scripts
│   ├── features/              # Feature engineering
│   ├── models/                # Model training and evaluation
│   └── visualization/         # Visualization scripts
├── tests/                     # Unit tests
├── .gitignore                 # Git ignore file
├── dvc.yaml                   # DVC configuration
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker compose configuration
└── kubernetes/                # Kubernetes manifests
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker
- Kubernetes (Minikube)
- Jenkins
- Airflow
- DVC
- MLflow

### Installation
1. Clone the repository:
```bash
git clone [https://github.com/maheera1/mlops-project]
cd [mlops_project]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize DVC:
```bash
dvc init
```

### Development Workflow
1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of changes"
```

3. Push your branch and create a Pull Request:
```bash
git push origin feature/your-feature-name
```

Development Workflow
--------------------

### Branching Strategy

We follow a structured Git workflow to streamline development and deployment across different environments. The branching strategy ensures smooth collaboration and clear versioning for features, testing, and production environments.


```         
             ┌────────────┐
             │   prod     │
             └────┬───────┘
                  ▲
                  │
             ┌────┴───────┐
             │   test     │
             └────┬───────┘
                  ▲
                  │
             ┌────┴───────┐
             │   dev      │
             └────┬───────┘
                  ▲
      ┌───────────┴────────────┐
      │ feature/model-tuning   │
      │ feature/data-cleaning  │
      └────────────────────────┘
```

#### Branch Descriptions:

-   **`dev`**: The development branch where active coding and feature development occur.

-   **`test`**: The QA branch used for testing and validation before pushing code to production. It reflects code ready for testing.

-   **`prod`**: The production branch, containing only stable, production-ready code. It reflects what is deployed in production environments.

-   **`feature/*`**: Feature branches created from `dev` for the development of individual features or bug fixes. Once work is completed, these branches are merged back into `dev`.

#### Workflow Steps:

1.  **Create a new feature branch from `dev`**:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/your-feature-name
```

2.  **Make changes, commit them, and push the branch**:

```bash
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

3.  **Create a Pull Request (PR)** to merge changes into `dev`. Once the feature is tested and validated, it can be merged into `test` and eventually into `prod`.

4.  **Merge `dev` into `test`** for QA validation:

```bash
git checkout test
git pull origin test
git merge dev
git push origin test
```

5.  **Merge `test` into `prod`** once it passes QA:

```bash
git checkout prod
git pull origin prod
git merge test
git push origin prod
```


### CI/CD Pipeline
The project uses GitHub Actions for CI and Jenkins for CD. The pipeline includes:
- Code linting
- Unit testing
- Docker image building
- Kubernetes deployment

### Monitoring
- MLflow for experiment tracking
- Airflow for workflow monitoring
- Kubernetes dashboard for deployment monitoring

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
