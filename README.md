# Zuno Library - Interview Challenge

This is a project for Zuno Interview Challenge. It is a books webapp that allows users to explore and view books as well as to see the book views on a chart.


## Getting started

To get started, you have to either download or clone the repository

```bash
git clone https://github.com/gxvr/zuno-library.git
```

You need to install Node.js and NPM as well as Python and pip if you don't have them yet. 

## Installing requirements

On the backend you need to install all needed dependecies. cd to **fastapi** on your termainal and run:

```bash
pip install -r requirements.txt
```

Likewise on the frontend cd to **web** directory then run:

```bash
npm install
```
and it will install all required dependecies.

NOTE: If you are getting error on postcss while running the app you can try the following commands

```bash
npm uninstall tailwindcss postcss autoprefixer

npm install tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9
```

## You're ready to go 🚀

Now your system should be ready for launch and serve our wonderful app. 

First, Start your backend server on *fastapi* directory by running:

```bash
uvicorn main:app --reload --port 5051
```
Then on frontend go to *web* directory and run following command:

```bash
npm run serve
```

To use your app, open your browser and go to http://localhost:5000/

Enjoy!


## Technologies
#### Frontend
- VueJs
- TailwindCSS
- ChartJS
- HTML5

#### Backend
- Python
- FastAPI
- SQLModel
- MYSQL
- Uvicorn

## TODO
- [ ] Showing the book views on a chart