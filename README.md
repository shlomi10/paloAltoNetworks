# Playwright Python Example

## Articles written about this project

## Project Setup

* Install pytest-html-reporter by running the following command:

```
pip install pytest-html-reporter
```

* Install Playwright by running the following command:

```
playwright install
```

* Install requirements (dependencies) by running the following command:

```
pip install -r requirements.txt 
```

* install Docker environment
* load the image with the following command:

```
docker load < home-task-dynamic-ip.tar
```

then run the following command to run the image:

```
docker run -d -p 3000:3000 -p 5000:5000 --name home-task home-task:amd64
```

* Clone the project
* Navigate to the project directory

## Running Tests with report

```
python -m pytest tests_ui_layout/ --html-report=./reports
```

When no browser was selected then chromium will be used.

* Run tests:

```
pytest
```

## Viewing Test Results

* View results locally by navigate to the reports folder under the main folder of the project

## View Help And Custom CLI Options

```
pytest --help
```