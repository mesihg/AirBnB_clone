# AirBnB Clone Project

## Description of the project

The project is a fullstack web application of AirBnB clone. The first part of the projects starts from building the console part and step by step build the entire web app.

## Part 1: Command interpreter

The first part of the project includes building the console or command line interpreter.

## Functionality of command interpreter
  In this part of the console application, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## Execution
### The shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

### But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```
## Some Resources

- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [packages concept page](https://alx-intranet.hbtn.io/concepts/66)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Authors

- Messih Grmay <[mesihg](https://github.com/mesihg)>
- Belay Tadese <[belaygithub](https://github.com/belaygithub)>
