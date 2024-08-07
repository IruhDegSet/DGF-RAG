# DGF-RAG
Projet interne a DGF technologies. 

## Project structure
rag-system/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow file
├── data/
│   ├── raw/                   # Raw data files
│   └── processed/             # Processed data files
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.yaml        # Configuration file
│   ├── data_ingestion/
│   │   ├── __init__.py
│   │   └── ingestion.py       # Data ingestion scripts
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   └── preprocess.py      # Data preprocessing scripts
│   ├── indexing/
│   │   ├── __init__.py
│   │   └── index.py           # Indexing scripts
│   ├── retrieval/
│   │   ├── __init__.py
│   │   └── retrieve.py        # Retrieval scripts
│   ├── generation/
│   │   ├── __init__.py
│   │   └── generate.py        # Generation scripts
│   ├── deployment/
│   │   ├── __init__.py
│   │   └── deploy.py          # Deployment scripts
│   └── utils/
│       ├── __init__.py
│       └── utils.py           # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_ingestion.py      # Unit tests for data ingestion
│   ├── test_preprocessing.py  # Unit tests for preprocessing
│   ├── test_indexing.py       # Unit tests for indexing
│   ├── test_retrieval.py      # Unit tests for retrieval
│   ├── test_generation.py     # Unit tests for generation
│   └── test_deployment.py     # Unit tests for deployment
├── scripts/
│   ├── train_model.py         # Script for training models
│   └── deploy.sh              # Deployment script
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Dockerfile for containerization
├── docker-compose.yml         # Docker Compose file
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
