<p>
<img width="200" src="https://lh4.googleusercontent.com/yUzaviDgzDIq4-ZHp9k0YU5fsz0nOdekNRt1qHgp7Qdlw5BNfe6bETEf5ZWd-Vkn_m57BPx7HcDrwFK41ptLnQLTNipWmTAtiQwZL_8s97Nkzn94xP7XVKb3RnV0fx8QEZoxlkVd" align="right" >
</p>

# AirBnB clone - The console

## The project

The AirBnB clone (hbnb), is a project in which the students of Holberton  deploy on a server a simple copy of the  [AirBnB website](https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A "AirBnB website"), in order to cover all fundamental concepts of the higher level programming track.

The web application is composed by:
<p>
<img width="300" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png" align="right" >
</p>
-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-   A website (the front-end) that shows the final product to everybody: static and dynamic
-   A database or files that store data (data = objects)
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The console

The console is a command line interpreter but limited to a specific use-case. In this case it will be able to manage the objects of our AirBnb clone  project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object                                                                                
### Execution (How to start it?)
The shell works like this in interactive mode:
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

But also in non-interactive mode:
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
### How to use it?
### Examples
### Authors

-   Emma Juliana Gachancipa Castelblanco
     [![alt text][1.1]][1][![alt text][2.1]][2][![alt text][3.1]][3][![alt text][4.1]][4]

-   Juan Sebastian Montealegre Calle
          [![alt text][1.1]][5][![alt text][2.1]][6][![alt text][3.1]][7][![alt text][8.1]][8]

[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[3.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)
[4.1]: https://i.imgur.com/TJRr1iY.png (linkedin)
[5.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[6.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[7.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)
[8.1]: https://i.imgur.com/TJRr1iY.png (linkedin)

[1]: http://www.twitter.com/julgachancipa
[2]: http://www.facebook.com/emmajuliana.gachancipa
[3]: https://plus.google.com/+CarlSednaoui
[4]: https://www.linkedin.com/in/emma-juliana-gachancipa-castelblanco-4b3667188
[5]: https://twitter.com/JSebastianCalle
[6]: https://www.facebook.com/juansebastian.calle
[7]: http://www.github.com/carlsednaoui
[8]: https://www.linkedin.com/in/juan-sebastián-montealegre-calle-3057155b
