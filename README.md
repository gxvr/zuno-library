# Zuno Library - Interview Challenge

This is a project for Zuno Interview Challenge. It is a books library webapp that allows users to view, search and explore books as well as to see the book views on a chart.


## Getting started

To get started, you have to either download or clone the repository

```bash
git clone https://github.com/gxvr/zuno-library.git
```

Then you have to install Virtualenv if you don't have it yet with

```bash
pip install virtualenv
```

Additionally you need to install Node.js and NPM if you don't have it yet. Go to NodeJs [website](https://nodejs.org/en/) and download the latest version.

Lastly, you need to install Vuejs CLI globally by

```bash
npm install -g @vue/cli
```

## Installing requirements

On the backend you need to install all needed dependecies. Go to **fastapi** directory and run:

```bash
pip install -r requirements.txt
```

Likewise on the frontend go to **web** directory then run following command:

```bash
npm install
```
and it will also install all required dependecies.

If you encountered error on postcss while running the app you can try the following commands

```bash
npm uninstall tailwindcss postcss autoprefixer

npm install tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9
```

## You're ready to go 🚀

Now your system should be ready for launch and serve our wonderful app. 

First, Start your backend server on *fastapi* directory by running:

```bash
uvicorn index:app --reload --port 5051
```
Then on frontend go to *web* directory and run following command:
```bash
npm run serve
```

To use your app, open your browser and go to http://localhost:5000/

Enjoy!


## Technologies
#### Frontend
- VueJs & Vue Router
- TailwindCSS
- ApexCharts
- HTML5/CSS3

#### Backend
- Python
- FastAPI
- MYSQL - pymysql
- SQLAlchemy
- Uvicorn
- VirtualEnv