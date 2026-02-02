## 🎭 Playwright-Python-Docker Framework
### Resilient, Scalable and Containerized E2E Test Automation

#### This repository serves as a Proof of Concept (PoC) for a high-performance test automation engine. It leverages the Page Object Model (POM) pattern and Docker to ensure that tests are not only maintainable but also architecturally decoupled from the local environment.

### 🚀 Key Advantages
#### Modern Browser Engine: Powered by Playwright for ultra-fast, reliable UI interaction.

##### Architectural Integrity: Strict Page Object Model (POM) implementation for high code reusability.

##### Infrastructure as Code: Fully containerized runtime ensures "it works on my machine" translates to "it works in CI".

##### Massive Scalability: Built-in support for parallel execution and cross-browser matrices.

### 🛠 Tech Stack
##### Core: Python 3.12+
##### Execution: Pytest
##### Automation: Playwright
##### Virtualization: Docker & Docker Compose
##### CI/CD Ready: Compatible with Jenkins, GitHub Actions and Bamboo

### 📂 Framework Architecture
```
├── pages/               # Page Objects
├── tests/               # Tests
├── conftest.py          # Global fixtures & setup logic
├── pytest.ini           # Test runner configurations
├── Dockerfile           # Image definition
└── docker-compose.yml   # Multi-container orchestration
```

### ⚡ Execution Guide
##### Standard Execution

Run the full suite or target specific tags:
```text
pytest                 # Run all tests
pytest -m smoke        # Run critical path only
```

#### Containerized Execution

Spin up the entire environment with a single command:
```text
docker compose up --build
```