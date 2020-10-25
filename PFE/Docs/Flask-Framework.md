<center><h1 style="color: #ff0000">Flask Framework</h1></center>

<h2>Definition</h2>

Flask is a Python framework available under the BSD license. It was inspired by the Sinatra Ruby framework. Flask depends on the Werkzeug WSGI toolkit and Jinja2 template.

The main idea behind Flask is to help build a solid web application foundation. From there, you can use any extensions you might need. Flask is chosen for any and all projects. In fact, it’s a default choice for any web project that isn’t a match for Django.

Flask’s lightweight and modular design makes it easily adaptable to developers’ needs. 


<h2>Features</h2>


Flask includes a number of useful out-of-the-box features:

•	Built-in development server and a fast debugger

•	Integrated support for unit testing

•	RESTful request dispatching

•	Jinja2 templating

•	Secure cookies support (client-side sessions)

•	WSGI 1.0 compliance

•	Unicode-based

•	Ability to plug in any ORM

•	HTTP request handling


<h2>What is REST?</h2>

The characteristics of a REST system are defined by six design rules:

- Client-Server: There should be a separation between the server that offers a service, and the client that consumes it.
 
- Stateless: Each request from a client must contain all the information required by the server to carry out the request. In other words, the server cannot store information provided by the client in one request and use it in another request.

- Cacheable: The server must indicate to the client if requests can be cached or not.

- Layered System: Communication between a client and a server should be standardized in such a way that allows intermediaries to respond to requests instead of the end server, without the client having to do anything different.

- Uniform Interface: The method of communication between a client and a server must be uniform.

- Code on demand: Servers can provide executable code or scripts for clients to execute in their context. This constraint is the only one that is optional.


<h2>What is a RESTful web service?</h2>

The REST architecture was originally designed to fit the HTTP protocol that the world wide web uses.

Central to the concept of RESTful web services is the notion of resources. Resources are represented by URIs. The clients send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

The REST design does not require a specific format for the data provided with the requests. In general data is provided in the request body as a JSON blob, or sometimes as arguments in the query string portion of the URL

<h2>Flask Installation Steps</h2>

1) Create a directory 

                              mkdir dir_name 

2) Create an environment

                             sudo apt install python3-pip

                             sudo apt install python3-venv 
             
                             sudo python3 -m venv env

3) Change the permission of virtuel environment 

                             sudo chown -R pi:pi env

4) check the permission of virtuel environment
       
                             stat env

5) Activate the environment

                            . env/bin/activate

6) Install Flask
             
                             pip install Flask

7) Create a minimal Flask application
           
                             nano Myapplication.py
           
8) Execute the application

                             export FLASK_APP=Myapplication.py

To enable all development features (including debug mode) you can export 

the FLASK_ENV environment variable and set it to development before running the server

                             export FLASK_ENV=development

If we want change the default port number (5000)
 
                             export FLASK_RUN_PORT=8000

If we have the debugger disabled or trust the users on our network, we can make 

the server publicly available simply by adding --host=0.0.0.0 to the command line

                             flask run --host=0.0.0.0 

9)deactivate the environment
   
                             deactivate

<h2>Sources</h2>

[Link 1](https://flask.palletsprojects.com/en/1.1.x/installation/)
[Link 2](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
[Link 3](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)
[link 4 ](https://flask.palletsprojects.com/en/1.1.x/appcontext/)
[Link 5](https://flask.palletsprojects.com/en/1.1.x/logging/)