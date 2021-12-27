# Zuno Library - Interview Challenge

This is a project for Zuno. It is a books library webapp that allows users to view, search and explore books as well as to see the book views on a chart.


## Getting started

To get started, you have to either download or clone the repository

```bash
git clone https://github.com/gxvr/zuno-library.git
```

Then you have to install Pipenv if you don't have it yet with

```bash
pip install pipenv
```

Also you need to install Node.js and NPM if you don't have it yet. Go to NodeJs [website](https://nodejs.org/en/) and download the latest version.

Lastly, you need to install Vuejs CLI globally by

```bash
npm install -g @vue/cli
```

## Installing requirements

On the backend you need to install all python requirements for zuno library to be able to run. install by following command:

```bash
pipenv install  (Change python version in Pipfile to match what you have installed in your computer before running this command) 
```

On the frontend you need all dependecies to be installed also. Got to **web** directory then run following command:

```bash
npm install
```

## Youre ready to go

Now you're setup should be ready for launch, if you're running this on local environment use:

```bash
pipenv run dev
```

while if you're running this on production environment use
```bash
pipenv run prod
```

## Technologies
#### Frontend
- VueJs
- TailwindCSS
- AlpineJS
- ApexCharts
- HTML5/CSS3

#### Backend
- Python
- FastAPI
- MYSQL
- SQLAlchemy
- Uvicorn
- Loguru