# Python Course 2026
This repository contains information about the course _"Basic Programming - Introduction into Python"_ (2026).  

## Acknowledgments
In this class, we will follow largely (but not exclusively) the course [NESC 3505 Neural Data Science](https://neuraldatascience.io/), developed at Dalhousie University as an open educational resource.

## Course structure
### Approach
The first part of the course follows an inverted classroom approach, which means you prepare the material for the sessions at home, leaving the actual sessions for doing exercises, discussions, questions, and problem-solving. The second part of the course - after the vacation - consistst of more advanced sessions that will address more specific topics, such as the use of AI, data processing and presentation for neuroscience, how to design (re)usable software and such.

### Schedule
<img src="https://github.com/eulerlab/python-course-2026/blob/main/pics/python_class_schedule_2026_v2.png" width="720" align="center"/>

### Materials
The materials consist of
- Online chapters, which will provide you with the respective background
- Jupyter notebooks, in which you can learn and practice Python concepts
- YouTube videos, which go through the notebooks step-by-step. We highly recommand to try to do the notebooks first by yourself, and only use the videos if you encounter major difficulties

When indicated below, you need to read a few chapters and do the lesson part of the respective Jupyter notebooks __before the session__. The notebooks are divided into a lesson part, where the concepts are introduced and demonstrated, and an exercise part, where you can apply the knowledge just gained. 

__During the sessions__, we will to the exercise parts of the notebooks together, discuss what you learned, where you encountered problems, and how to solve these.

> _Important: The links to chapters point at the original class material, whereas the notebooks you will find in your `bwJupyter` environment - as demonstrated in the first session._

### Important link(s)
[Link to bwJupyter environment](https://hub.bwjupyter.de/services/profilemanagement/add?profile=617d20c6-5216-4ab8-bf77-0f652278c3d8)  

## 17.4. | Introduction, Setup, Project overview
__To prepare before:__
- Read chapters ["About This Course"](https://neuraldatascience.io/intro/why/) (all sections) and ["Introduction to Data Science"](https://neuraldatascience.io/nds/what-is-nds/) (all sections)

__During the class:__
- _Why this course?_ About adult learners and your motivation to learn Python, your programming/Python background, that the only way to learn to code is to write it, the importance of coding skills for science and beyond, and the use of AI tools.
- _The organisation of this course._ Time budget outside the classroom, videos as the last resort, and final project.
- _Setting up `bwJupyter.de`__ and accessing the course material. How to submit exercises.
- _Skills evaluation_

## 24.04. | Variables & Assignment, Data Types & Conversion, Python Built-ins, Lists (, Dictionaries)
__To prepare before:__
- Read chapter ["Introducing Python"](https://neuraldatascience.io/python/introduction/); you can ignore the section `Deactivate AI for Now`. Also, read the next chapter with the respective learning objectives.
- On bwJupyter: Go over the notebooks `01 - Variables and Assignments` to `05 - Dictionaries` under `__shared`. Note that the exercise parts of the notebooks will be done in class.

__During the class:__
- Do exercises together, answer qustions.

## 08.05. | Dictionaries, For loops, Conditionals, pandas, Looping over datafiles
__To prepare before:__
- On bwJupyter: Go over the notebooks `06 - For Loops` and `09 - Looping Data Files` under `__shared`.

__During the class:__
- Do exercises together, answer qustions.
- For more advanced students, there will be additional, more challenging exercises (check out the `extra_execises` folder)

## 15.05. | Numpy and Scipy
__To prepare before:__
- On bwJupyter: Go over the notebook `08 - pandas DataFrames`
- Go over the official [numpy tutorial](https://numpy.org/doc/2.4/user/absolute_beginners.html)
- On bwJupyter: Go over the notebook `10 - Numpy and Scipy` (no need to do the tasks, we will do them together in the class)

__During the class:__
- We will go through the notebook and do the tasks in the notebook

## 22.05. | Data Visualization using Matplotlib (1/2)
__To prepare before:__
- Read chapter ["Introduction to Data Visualization"](https://neuraldatascience.io/4-viz/introduction.html) and the respective learning objectives.

__During the class:__
- We will go through the Jupyter notebook together.
- In the end, as an exercise, you should re-create a figure including different plot types based on real data

## 05.06. | Data Visualization using Matplotlib & Seaborn (2/2)
__To prepare before:__
- Do the notebook lecture from the last session on your own again
- Read chapter ["Data Science Plots with Seaborn"](https://neuraldatascience.io/viz/seaborn/) and the respective learning objectives.

__During the class:__
- We will build the figures from the last session together step-by-step
- Discuss and showcase Seaborn

## 12.06. | IDEs and coding with AI
__To prepare before:__ 
1) An IDE (Integrated Development Environment) is a program where you have all you need to write, read, and run code effectively. We will talk about this more in the lecture, but as a preparation please try to install one very common IDE called "visual studio code": Install visual studio code [here](https://code.visualstudio.com/download).
2) In VS code there are some very useful extensions specifically for working with Python and Jupyter notebooks. After installing VS code, go to the "Extensions marketplace" (block-like icon on the left hand pannel) and install the "Python" and "Jupyter" extensions. These extensions add helpful features, but they don't include Python itself. Note that after installing the "Python" extension, VS code may ask you somthing like "No Python found. Would you like to install uv and use it to install python?". Please only click "install" here, if it expicitly mentions "uv". If you clicked "install" you can then skip the next step.
3) UV is a piece of software that allows you to donwload Python itself as well as packages like numpy.  If VS code did not offer you to install "uv", please install uv [here](https://docs.astral.sh/uv/getting-started/installation/). You will have to open either PowerShell (Windows) or Terminal (Mac/Linux) and paste the line of code for your operating system into there. Afterwards, close and open PowerShell/Terminal again and type in "uv --version", to see if it works. In the lecture we will then use uv to install python.

If this did not work for you, do not worry! At the beginning of the class, there will be some time to trouble shoot of finish installing, but it is important that you try for yourself first at home.

__During the class:__
- We will explain concepts like IDEs and environments. 
- You will get some hands on experimence in running code on your computer and using IDEs, which will be super useful to you if you have to deal with code during your lab rotations.
- If time, we will discuss how to use AI effectively while coding and you will again get some hands on experimence in "vibe coding".

## 19.06. | Git(Hub)
__To prepare before:__ 
Look at the [slides](https://github.com/eulerlab/python-course-2026/blob/main/material/Lecture%20GitHub%20-%20Python%20course_2026.pdf) for the session.

__During the class:__
- We will explain why distributed version control software like `Git` is useful and how it works on platforms, such as `GitHub`.
- You will learn to set up a simple Git repository and work with it.

__Material from the class:__
Here are the [slides](https://github.com/eulerlab/python-course-2026/blob/main/material/Lecture_GitHub_version_Jane.pdf) and the [notes](https://github.com/eulerlab/python-course-2026/blob/main/material/Lecture_Github_notes_Jane.pdf) from the session.

## 27.06. | Exploratory Data Analysis
__To prepare before:__ 
Please read the following sections of the Neural Data Science course book:
- ["Working with Repeated Measures"](https://neuraldatascience.io/eda/repeated-measures/): Understand the code for generating the plots and pay close attention to the "Aggregating using Split-Apply-Combine" part. We will need this in the lecture.
- ["Data Cleaning - Dealing with Outliers"](https://neuraldatascience.io/eda/data-cleaning/): Understand the code they use for grouping and cleaning data.
-  ["Basic Statistics in Python: t tests with SciPy"](https://neuraldatascience.io/eda/ttests/): Read this section up to "One-sample t tests".

__During the class:__
We will apply what you learn from the readings to another familiar dataset. 


## 03.07. | Techniques for preventing and fixing bgus
__To prepare before:__ 
Before the lecture, think about the following questions:
- What do you expect of code that is used for scientific papers, and that is used in research labs to analyse data?
- How much time do you spend writing code, and how much time do you spend reading and trying to understand code?
- What strategies do you currently use when your code does not behave as expected?

__During the class:__
We will talk about these questions in class and will go through techniques like assertions, automatic tests, and human and LLM-based code review.
