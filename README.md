# gbg-python-user-group

## Introduction

* This a mainly online group for python resource sharing and helping

## Learning resources

### Learning python

Introductory resources
* [Codecademy: Python](http://www.codecademy.com/tracks/python) - Gentle and interactive introduction to Python basics, step-by-step construction of complex programs from simpler building blocks.
* [Learn Python the hard way](http://learnpythonthehardway.org/book/)
* [Coursera: Python for Genomic Data Science](https://www.coursera.org/course/genpython) - Free online course starting July 6th, 2015 (sign up!)

Video resources

### Learning git

In this user group we use Github to share and mutually edit code. In case you don’t have a Github account yet, register on [Github](https://github.com/) and explore how Github works. Github is an online forum where people share code and work together on joined projects (also referred to as the Facebook for nerds). Additionally it is recommendable to download a software package that enables you to use Git interactively through the command-line. You can download this software [here](https://git-scm.com/downloads)    
Now after the software is installed  you can use the several Git commands to easily download, change and upload files from and to Github (for Windows users, use the bash terminal that comes with the Git-download).  
Download the github repository:  
'git clone https://github.com/mtop/gbg-python-user-group.git'  
Download newest changes (update):  
'git pull'  
You can edit any files on your local copy of the github directory. If you want to upload your changes you will have to go through the following steps. It is good practice and very important to create a personal branch on which you work and save your changes. If you want to apply those changes to the main branch (master) you can merge your branch with the master branch. This procedure avoids conflicting edits, which occur when multiple people work on the same document in parallel.  
Create a new branch:  
'git checkout -b nameofbranch'  
Switch to a specific branch:  
'git checkout nameofbranch'  
Check, which branch you are currently on:  
'git branch'  
You can now work on the files that you have downloaded from Github. After you saved all the changes in the edited document you need to commit these changes to your Git. It is good practice to drop a quick line of which changes you are committing so that other people understand the purpose of your update:  
'git commit -m “describe what you did” nameoffile'  
Any changes that are committed will be saved to your current branch. You can now upload them to Github:  
'git push'  
If you want to save your commits to the master branch, you will need to join your branch with the master branch. For this purpose you must connect back to the master branch:  
'git checkout master'  
Now join your local branch to master:  
'git merge nameofbranch'  
Now you need to commit and push again in order for your changes to show in the main document of the master branch.  


More advanced coding can be learned by using it in your own bioinformatics project or solving coding problems. There are many websites that offer coding problems, such as [Simple Programming Problems](http://adriann.github.io/programming_problems.html), [46 Simple Python Exercises](http://www.ling.gu.se/~lager/python_exercises.html), [Rosetta Code](http://rosettacode.or/wiki/Category:Programming_Tasks), and many more.
