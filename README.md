# AirBnB clone

The Airbnb clone project replicates a mini-version of the Airbnb website for learning purposes.
It includes:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### Final product
![final image](/assets/airbnb_clone)

### Data diagram
![data diagram](assets/data_diagram)

### Tools
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Ubuntu">
</a>
<!-- bash -->
<a href="https://www.gnu.org/software/bash/" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal">
</a>
<!-- python-->
<a href="https://www.python.org" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python">
</a>
<!-- pycodestyle -->
<a href="https://pycodestyle.pycqa.org/en/latest/" target="_blank">
  <img src="https://img.shields.io/static/v1?label=&message=pycodestyle&color=2B5B84&logo=Python&logoColor=3776AB&labelColor=2F333A" alt="pycodestyle">
</a>
<!-- vim -->
<a href="https://www.vim.org/" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Vim">
</a>
<!-- git -->
<a href="https://git-scm.com/" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system">
</a>
<!-- github -->
<a href="https://github.com" target="_blank">
  <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">
</a>
<!-- Style guidelines -->

### Style
[PEP8](https://pep8.org/)

## 1 - The console
The console is a command interpreter that enables developers to manage objects in the project from a command-line interface. With it you can:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

![console](/assets/the_console.png)

### Usage
Interactive mode

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
Non Interactive mode
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

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

* create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
(hbnb) create BaseModel
57262839-51d7-4a9a-93e2-35ed8e91d823
$
```

* show 

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb)
(hbhb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) all
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb) all BaseModel
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
```
* destroy

>*Deletes an instance of a given class with a given ID.*
>*Update the file.json*

```bash
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
(hbnb) all
[]
```

* count 

> *Prints the number of instances of a given class.*

```bash
(hbnb) create User
ce5f7ac5-4b2e-4c90-933d-6c78e69ab1c7
(hbnb) create User
dd697519-4ac9-42e0-80e2-fa7b3ac61193
(hbnb) create User
52c4036b-f018-49d0-8d93-d7a2d56bcdad
(hbnb) count User
3
```

### Objects
| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains test files for AirBnb Clone |
|  | console.py | Command line Interpreter for managing AirBnB objects |
| models | base_model.py | Defines all common attributes/methods for other classes |
| models | amenity.py | Creates class `amenity` |
| models | city.py | Creates class `city` |
| models | place.py | Creates class `place` |
| models | review.py | Creates class `review` |
| models | state.py | Creates class `state` |
| models | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |

## Authors
List of authors can be found in the `AUTHORS` document
