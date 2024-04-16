# Multi-Configuration-Scanner

# System Design Multi-Configuration-Scanner:
![image](https://github.com/ShakuriAvi/Multi-Configuration-Scanner/assets/65177459/6bae7700-6b90-49c1-aea9-77363a2cd3cf)
To run the project, you need pull the main, install the requirements file and add a cfg.py file (I will attach a picture below of how the file should look).

![image](https://github.com/ShakuriAvi/Multi-Configuration-Scanner/assets/65177459/e2a763f9-1d7e-4c49-9eee-34e11d114138)


![image](https://github.com/ShakuriAvi/Multi-Configuration-Scanner/assets/65177459/08292841-acad-45d0-89d0-85b245c0566e)


You need add a permission to your repository.
* About the Ptoject:
The project is based on the thread producer-consumer design pattern(although not with a queue, but I used a generator that provides tasks and some workers that pull and execute them when they are free). I also used Factory to support different types of files and add them without changing any code.  I kept the SOLID principles throughout the project with the help of inheritance and abstract classes. It was really nice to learn how to work with PR in front of Git using the PYGitHub library (we use AWS). My focus is on the design and working on a large scale. There are three algorithms I implemented in order to update the user whose configuration needs to be changed:
To begin with, I checked if one of the files contained an implementation of a secret variable in AWS. It causes damage to the company's systems and penetration of information. If it exists, I deleted the value of the variable.
The second, checking the connection to the system, whether unauthorized aliens are contained within authorized aliens. If so, I deleted it from the list. 
The third one is a little more complex, I used a library that checks requirements files, if one of the values in the library is incorrect, it gives suggestions for optimization. In this case, I didn't have time to delve deeper and understand how I change a version in the requirements, but I created a new branch and indicated to the user what the recommendations are regarding the versions.
