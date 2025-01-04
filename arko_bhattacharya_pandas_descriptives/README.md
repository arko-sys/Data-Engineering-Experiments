[![Run Tests](https://github.com/nogibjj/arko_bhattacharya_week1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/arko_bhattacharya_week1/actions/workflows/test.yml)

# Pandas Descriptive Statistics

This project is to demonstrate how to create a visualization on CSV input files. We then bake in CICD functionality to profile our dataset at CICD runtime.

## Project Function
- Read the "VCT'21 Map Ban Dataset"
- Create a visualization , depicting the distribution of the banned maps.
- Profile the dataset as a CICD process (output as report.md).

![image](https://github.com/user-attachments/assets/a2dd49f2-f48c-47b1-95a5-30fb271af230)
![image](https://github.com/user-attachments/assets/3b902ade-c779-4dd4-b6a2-a14b467bf29a)




## Project Structure

- `scripts/`: Contains the source code for the project.
- `tests/`: Contains the unit tests for the project.
- `data/`: Contains the input data files.
- `requirements.txt`: Lists the Python dependencies.
- `Makefile`: Defines common tasks like installing dependencies, running tests, linting, and running docker.
- `.devcontainer/`: Contains `Dockerfile` and VS Code configuration.
- `.github/workflows/`: Contians CI/CD workflows for GitHub.

## Project Setup
### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/nogibjj/arko_bhattacharya_pandas_descriptives.git
cd arko_bhattacharya_pandas_descriptives
```
![image](https://github.com/user-attachments/assets/a66f20ea-69cf-4354-8649-e03e62f4451c)



### 2. Dockerize

Build and Run the Docker image:

```bash
docker build -f .devcontainer/Dockerfile -t <image-name> .
docker run -it --rm -v $(pwd):/app <image-name> /bin/sh
```
![image](https://github.com/user-attachments/assets/6ebd6d64-d3d0-4968-8ad5-4e0642a7f702)


## GitHub CI/CD Setup
- `.github/workflows/`: Contians CI/CD workflows for GitHub, which triggers when pushing code to the GitHub repo. 
Writes analysis report to `report.md` file.

[![Run Tests](https://github.com/nogibjj/arko_bhattacharya_week1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/arko_bhattacharya_week1/actions/workflows/test.yml)

![image](https://github.com/user-attachments/assets/a633abe3-da89-44e8-818d-2f6b12b98ac3)

  





