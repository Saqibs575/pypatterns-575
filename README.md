# **pypatterns-575: Unlock a world of intricate pattern creation in Python** <br>



[![PyPI version](https://badge.fury.io/py/pypatterns-575.svg)](https://badge.fury.io/py/pypatterns-575) 
[![PyPI](https://img.shields.io/pypi/v/pypatterns-575)](https://pypi.org/project/pypatterns-575/)
[![PyPI - License](https://img.shields.io/pypi/l/pypatterns-575)](https://pypi.org/project/pypatterns-575/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pypatterns-575)](https://pypi.org/project/pypatterns-575/)
[![PyPI - Status](https://img.shields.io/pypi/status/pypatterns-575)](https://pypi.org/project/pypatterns-575/)
![PyPI Downloads](https://img.shields.io/pypi/dm/pypatterns-575)
[![Total Downloads](https://static.pepy.tech/personalized-badge/pypatterns-575?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/pypatterns-575)


![GitHub](https://img.shields.io/github/license/Saqibs575/pypatterns-575)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Saqibs575/pypatterns-575?label=Pull%20Requests)](https://github.com/Saqibs575/pypatterns-575/pulls)
[![GitHub issues](https://img.shields.io/github/issues/Saqibs575/pypatterns-575?label=GitHub%20Issues)](https://github.com/Saqibs575/pypatterns-575/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub last commit](https://img.shields.io/github/last-commit/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575/commits/main)
[![GitHub contributors](https://img.shields.io/github/contributors/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575/graphs/contributors)
[![GitHub code size](https://img.shields.io/github/languages/code-size/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575)
[![GitHub stars](https://img.shields.io/github/stars/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575/network)
[![GitHub top language](https://img.shields.io/github/languages/top/Saqibs575/pypatterns-575)](https://github.com/Saqibs575/pypatterns-575)

-----------------------------
-----------------------------

## **What is it ?**

The "`pypatterns-575`" package stands as a robust and feature-rich Python library meticulously crafted to streamline and expedite the process of generating and displaying a diverse array of patterns. By leveraging the power of simple characters like asterisks ("*"), numbers, and alphabets, this package brings the art of pattern creation to your fingertips. Its primary goal is to provide developers, students, and enthusiasts with a seamless and efficient way to conjure intricate patterns that range from classic pyramids to elegantly crafted hollow pyramids, triangles of varying orientations, intricate hollow triangles, captivating rhombuses, dazzling diamonds, and much more.

Rooted in the idea of empowerment, the "`pypatterns-575`" package equips individuals with the tools they need to effortlessly embark on the creative journey of pattern design. With a focus on accessibility and user-friendliness, the package offers an intuitive interface that makes pattern generation and printing a delightful experience. The package's design philosophy centers around the belief that even those new to programming or pattern creation can dive in with confidence.


---------------------------
---------------------------

## **Table of Contents**

- [Project Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
   - [Window Users](#windows)
   - [macOS Users](#macOS)
   - [Linux Users](#linux)
- [Usage](#usage)
    + [Star Patterns](#star-patterns)
      * [Pyramid](#pyramid)
      * [Triangle](#triangle)
      * [Diamond](#diamond)
    + [Number Patterns](#number-patterns)
      * [Pascal's Triangle](#pascal)
      * [Triangle1](#triangle1)
      * [Triangle2](#triangle2)
      * [Pyramid1](#pyramid1)
    + [Alphabet Patterns](#alphabet-patterns)
      * [Triangle](#alpha-triangle)
      * [Pyramid1](#alpha-pyramid1)
      * [Pyramid2](#alpha-pyramid2)
   + [Pattern Code](#pattern-code)
- [Contributing](#contributing)
- [License](#license)


------------------------------
------------------------------


## **Project Architecture** <a name = 'architecture'></a>

```
WORKSPACE
    |
    |--> pypatterns
    |        |
    |        |--> alphabet_patterns
    |        |         |
    |        |         |--> __init__.py
    |        |
    |        |--> get_pattern_code
    |        |         |
    |        |         |--> base_list.py
    |        |
    |        |--> number_patterns
    |        |         |
    |        |         |--> __init__.py
    |        |
    |        |--> star_patterns
    |        |         |
    |        |         |--> base_list.py
    |        |
    |        |--> __init__.py
    |   
    |
    |--> examples.ipynb
    |
    |--> .gitignore
    |
    |--> LICENSE
    |
    |--> banner.png
    |
    |--> README.md
    |
    |--> requirements.txt
    |
    |--> setup.py

```

---------------------------
---------------------------

# **Features**

## **Diverse Patterns:**
`pypatterns-575` offers an array of pattern types, ranging from symmetric pyramids to hollow triangles, rhombuses, diamonds, and more. Each pattern type is implemented as a separate function, ensuring that users can easily choose and generate the specific pattern they need.

---------------------------
## **Customization:** 
The package provides a range of customizable parameters for each pattern-generating function. Users can adjust parameters such as the number of rows, symbols used for the pattern, and even the starting character for alphabet patterns. This customization feature allows users to tailor patterns to suit specific project requirements or educational purposes.

While the package excels in creating patterns using asterisks ("*"), it also supports numbers and alphabets. This flexibility allows you to generate patterns that incorporate different symbols according to your needs.

---------------------------
## **Ease of Use:**
The package includes functions with intuitive names and clear parameters, making it suitable for developers of all skill levels, including beginners.

---------------------------

## **Simplified Pattern Generation**
The primary goal of `pypatterns-575` is to streamline the process of generating intricate patterns. By providing a collection of ready-to-use functions, the package eliminates the need to manually write code for pattern creation. This is particularly beneficial when creating patterns that involve repetitive logic, as the package handles the complexity while allowing users to focus on the desired pattern itself.

---------------------------
## **Clear and Comprehensive Parameters**
The functions provided by `pypatterns-575` are designed with clear and well-documented parameters. These parameters allow users to customize various aspects of the generated patterns, such as the number of rows, symbols used, and alignment. By offering parameter descriptions and default values, the package minimizes confusion and encourages experimentation.

---------------------------
## **Educational Tool**
With its ability to visualize programming concepts in a creative manner, `pypatterns-575` serves as an effective educational tool. Educators can leverage the package to visually demonstrate how loops, conditions, and structured programming constructs influence the output of patterns. This hands-on approach can enhance understanding and engagement among students learning programming fundamentals.

---------------------------
## **Streamlined Logic and Repetition**
Under the hood, `pypatterns-575` handles the intricate logic and repetitive code required for pattern generation. This abstraction simplifies the user's role to choosing a pattern, adjusting parameters if necessary, and invoking the corresponding function. Users can rely on the package's optimized and tested logic to produce accurate and visually appealing patterns.

---------------------------
## **Examples and Explainations**
The `pypatterns-575` package includes comprehensive examples that guide users through the process of creating various patterns. These resources demonstrate the usage of each function, showcase different parameter combinations, and provide insights into how patterns change based on user input. This educational content accelerates the learning curve, enabling users to quickly master the pattern generation process.

---------------------------
## **Compatibility with Learning and Exploration**
Due to its user-friendly nature, the package is especially suitable for educational environments. Beginners can grasp programming concepts more easily by observing the direct relationship between pattern output and parameter adjustments. This hands-on experience encourages exploration and experimentation, fostering a deeper understanding of programming fundamentals.

---------------------------
## **Seamless Integration**
Integrating `pypatterns-575` into existing projects is a straightforward process. Users can install the package with a single command using pip, and then effortlessly import the desired pattern functions into their codebase. This seamless integration allows developers to enhance their projects with visually striking patterns without significant coding effort.

---------------------------
## **Source Code Exploration**
To further enhance its educational value, `pypatterns-575` includes a unique get_pattern_code module. This module provides users with the ability to inspect the source code of each pattern-generating function. This feature allows users to delve into the internal workings of the package, promoting a deeper understanding of the pattern generation process.

However, I strongly recommend that you try to write the code on your own. Avoid directly exploring the 'get_pattern_code' module. Attempt to generate the patterns independently. If you encounter difficulties, you can refer to the source code. This practice will not only enhance your problem-solving skills but also boost your logical thinking abilities.

Working through the challenges of generating patterns manually allows you to develop a deeper understanding of the underlying logic. This understanding is invaluable when it comes to tackling more complex programming tasks. Moreover, by engaging in independent problem-solving, you'll gain the confidence to approach coding challenges with creativity and innovation

Learning to identify and rectify errors in your code is a crucial skill in programming. It enables you to develop resilience in the face of challenges and cultivates a growth mindset.

In conclusion, while the `'get_pattern_code'` module might provide a shortcut, the real value lies in the journey of crafting the solutions yourself. So, embrace the process, overcome challenges, and remember that every obstacle you encounter is an opportunity for growth.

---------------------------
---------------------------

# **Installation** <a name = "installation"></a>
To start using `pypatterns-575`, you can easily install it using the popular Python package manager, `pip`:

To get started with creating captivating patterns using the `pypatterns-575` package, follow these steps based on your operating system:

---------------------------
## **Windows Users** <a name = "windows"></a>
**Update `pip` (if needed)**: 
Open the Command Prompt as an administrator by searching for "cmd" in the Start menu, right-clicking on "Command Prompt," and selecting "Run as administrator." Then, execute the following command to update pip:

```python
python -m pip install --upgrade pip
```

**Install the Package**: In the same Command Prompt, execute the following command to install the `pypatterns-575` package:
```python
pip install pypatterns-575
```
---------------------------

## **macOS Users** <a name = "macOS"></a>
**Update `pip` (if needed)**: Open the Terminal and execute the following command to update pip:

```python
python3 -m pip install --upgrade pip
```
**Install the Package**: In the same Terminal, execute the following command to install the `pypatterns-575` package:

```python
pip3 install pypatterns-575
```
---------------------------

## **Linux Users** <a name = "linux"></a>
**Update `pip` (if needed)**: Open the Terminal and execute the following command to update pip:

```python
python3 -m pip install --upgrade pip
```
**Install the Package**: In the same Terminal, execute the following command to install the `pypatterns-575` package:

```python
pip3 install pypatterns-575
```

---------------------------

Once the installation is complete, you're ready to explore the world of intricate pattern design! For usage instructions and examples on how to create various patterns using the `pypatterns-575` package, please refer to the [Usage Guide](https://github.com/Saqibs575/pypatterns-575#usage-).

Refer to the documentation and examples provided in the readme.md and documentation files for detailed instructions on using the package to create various patterns.

Feel free to experiment with different pattern options and let your creativity shine. Happy pattern designing!


---------------------------
---------------------------


# **Usage** <a name = "usage"></a>
All types of patterns can be found in pypatterns file of `pypapatterns-575` package. You nedd to import the module every time before you are using it after successful installation;

```python
pip install pypatterns-575
```
```python
from pypatterns import star_patterns
```
---------------------------
---------------------------


# **Star Patterns** <a name = 'star-patterns'></a>

## **Pyramid** <a name = "pyramid"></a>

```python
star_patterns.get_star_pyramid()
```
### Output of the above code is ;

```python
             * 
          *  *  * 
       *  *  *  *  * 
    *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------


```python
star_patterns.get_star_hollow_pyramid()
```
### Output of the above code is ;

```python

        * 
      *   *
    *       *
  *           *
* * * * * * * * *  
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------


### You can pass arguments as well ;

```python
star_patterns.get_star_pyramid(n = 10 , inverted = True)

```

### Output of the above code is;

```python

 *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
    *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
       *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
          *  *  *  *  *  *  *  *  *  *  *  *  * 
             *  *  *  *  *  *  *  *  *  *  * 
                *  *  *  *  *  *  *  *  * 
                   *  *  *  *  *  *  * 
                      *  *  *  *  * 
                         *  *  * 
                            * 
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------

```python
star_patterns.get_star_hollow_pyramid(n = 10 , inverted = True)
```

### Output of the above code is;

```python
* * * * * * * * * * * * * * * * * * * 
  *                               *
    *                           *
      *                       *
        *                   *
          *               *
            *           *
              *       *
                *   *
                  * 

```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

---------------------------
---------------------------

## **Triangle** <a name = "triangle"></a>

```python
star_patterns.get_star_triangle()
```
### Output of the above code is ;

```python
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------

```python
star_patterns.get_star_triangle(n = 6, inverted = True)
```
### Output of the above code is ;
```python
*  *  *  *  *  *
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------

```python
star_patterns.get_star_hollow_triangle(n = 7)
```
### Output of the above code is ;
```python
* 
* *
*   *
*     *
*       *
*         *
* * * * * * *   
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------
------------------------------------


## **Diamond** <a name = "diamond"></a>

```python
star_patterns.get_star_diamond()
```
### Output of the above code is ;

```python
             * 
          *  *  * 
       *  *  *  *  * 
    *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
    *  *  *  *  *  *  * 
       *  *  *  *  * 
          *  *  * 
             * 
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

```python
star_patterns.get_star_hollow_diamond(n = 7)
```
### Output of the above code is ;
```python
              *
            *   *
          *       *
        *           *
      *               *
    *                   *
  *                       *
*                           *
  *                       *
    *                   *
      *               *
        *           *
          *       *
            *   *
              * 
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

```python
star_patterns.get_star_diamond2()
```
### Output of the above code is ;
```python
              *   
           *     *   
        *     *     *   
     *     *     *     *   
  *     *     *     *     *   
     *     *     *     *   
        *     *     *   
           *     *   
              *  
```


[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

## **GET ALL START PATTERNS** 

```python
# LET'S PRINT ALL STAR PATTERNS IN ONE STROKE WITH DEFAULT ARGUMENTS
from pypatterns.star_patterns import *

for func in dir(star_patterns) :
    if callable(getattr(star_patterns, func)) :
        globals()[func]()
```
### Output of the above code is ;
```python

*  *  *  *  *  
*           *
*           *
*           *
*  *  *  *  *  

         *  *  *  *  * 
       *           *
     *           *
   *           *
 *  *  *  *  * 

*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *  
*  *  *  *  *  

         *  *  *  *  * 
       *  *  *  *  * 
     *  *  *  *  * 
   *  *  *  *  * 
 *  *  *  *  * 

             * 
          *  *  * 
       *  *  *  *  * 
    *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 
    *  *  *  *  *  *  * 
       *  *  *  *  * 
          *  *  * 
             * 

              *   
           *     *   
        *     *     *   
     *     *     *     *   
  *     *     *     *     *   
     *     *     *     *   
        *     *     *   
           *     *   
              *   

        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *

        * 
      *   *
    *       *
  *           *
* * * * * * * * * 

* 
* *
*   *
*     *
* * * * * 

             * 
          *  *  * 
       *  *  *  *  * 
    *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  * 

         *  
       *   *  
     *   *   *  
   *   *   *   *  
 *   *   *   *   *  

*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  

*               *
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
*               *
 
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

---------------------------

```python
# LET'S PRINT ALL STAR PATTERNS IN ONE STROKE WITH INVERTED ARGUMENT

for func in dir(star_patterns) :
    if callable(getattr(star_patterns, func)) :
        if globals()[f'{func}'].__code__.co_varnames[1] == "inverted" :
            globals()[func](inverted = True)
        print()
```
### Output of the above code is ;
```python

 *  *  *  *  * 
   *           *
     *           *
       *           *
         *  *  *  *  * 


 *  *  *  *  * 
   *  *  *  *  * 
     *  *  *  *  * 
       *  *  *  *  * 
         *  *  *  *  * 




* * * * * * * * * 
  *           *
    *       *
      *   *
        * 

* * * * * 
*     *
*   *
* *
* 

 *  *  *  *  *  *  *  *  * 
    *  *  *  *  *  *  * 
       *  *  *  *  * 
          *  *  * 
             * 

 *   *   *   *   *  
   *   *   *   *  
     *   *   *  
       *   *  
         *  

*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  


 
```


[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


---------------------------
---------------------------


# **Number Patterns** <a name = 'number-patterns'></a>

```python
from pypatterns import number_patterns
```

## **Pascal's Triangle** <a name = "pascal"></a>

```python
number_patterns.get_pascal_triangle(n = 10)
```
### Output of the above code is ;

```python
                                             1         
                                        1         1         
                                   1         2         1         
                              1         3         3         1         
                         1         4         6         4         1         
                    1         5         10        10        5         1         
               1         6         15        20        15        6         1         
          1         7         21        35        35        21        7         1         
     1         8         28        56        70        56        28        8         1         
1         9         36        84        126       126       84        36        9         1  
```


[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------


## **Triangle1** <a name = "triangle1"></a>

```python
number_patterns.get_triangle1()
```
### Output of the above code is ;

```python
1   
2   3   
4   5   6   
7   8   9   10  
11  12  13  14  15 
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

## **Triangle2** <a name = "triangle2"></a>

```python
number_patterns.get_triangle2(n = 8)
```
### Output of the above code is ;

```python
1   
2   3   
3   4   5   
4   5   6   7   
5   6   7   8   9   
6   7   8   9   10  11  
7   8   9   10  11  12  13  
8   9   10  11  12  13  14  15  
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

## **Pyramid1** <a name = "pyramid1"></a>

```python
number_patterns.get_pyramid1(inverted = True)
```
### Output of the above code is ;

```python
1  2  3  4  5  4  3  2  1  
   1  2  3  4  3  2  1  
      1  2  3  2  1  
         1  2  1  
            1 
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------
------------------------------------

# **Alphabet Patterns** <a name = 'alphabet-patterns'></a>

```python
from pypatterns import alphabet_patterns
```

## **Triangle** <a name = "alpha-triangle"></a>

```python
alphabet_patterns.get_alpha_triangle()
```
### Output of the above code is ;

```python
A  
B  C  
D  E  F  
G  H  I  J  
K  L  M  N  O 
```
[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------


## **Pyramid1** <a name = "alpha-pyramid1"></a>

```python
alphabet_patterns.get_alpha_pyramid1(inverted = True)
```
### Output of the above code is ;

```python
A  B  C  D  E  F  G  H  I  
   J  K  L  M  N  O  P  
      Q  R  S  T  U  
         V  W  X  
            Y
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)


------------------------------------


## **Pyramid2** <a name = "alpha-pyramid2"></a>

```python
alphabet_patterns.get_alpha_pyramid2(n = 10)
```
### Output of the above code is ;

```python
                  A   
                B   C   
              D   E   F   
            G   H   I   J   
          K   L   M   N   O   
        P   Q   R   S   T   U   
      V   W   X   Y   Z   A   B   
    C   D   E   F   G   H   I   J   
  K   L   M   N   O   P   Q   R   S   
T   U   V   W   X   Y   Z   A   B   C 
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

---------------------------
---------------------------


# **Pattern Code** <a name = 'pattern-code'></a>

```python
from pypatterns import get_pattern_code
```

```python
get_pattern_code.get_star_triangle_code()
```
### Output of the above code is ;

```python
def get_star_triangle(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            print("*  " * i)
        return

    for i in range(n , 0 , -1) :
        print("*  " * i)
get_star_triangle() 
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

```python
get_pattern_code.get_pyramid1_code()
```
### Output of the above code is ;

```python
def get_pyramid1(n = 5 , inverted = False) :
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    if inverted == False :
        for i in range(1 , n+1) :
            print(3*" " * (n - i) , end = "")
            for j in range(1 , i + 1) :
                print(str(j).ljust(3) , end = "")
            for k in range(i-1 , 0 , -1) :
                print(str(k).ljust(3) , end = "")
            print()
        return

    for i in range(n , 0 , -1) :
        print(3*" " * (n - i) , end = "")
        for j in range(1 , i + 1) :
            print(str(j).ljust(3) , end = "")
        for k in range(i-1 , 0 , -1) :
            print(str(k).ljust(3) , end = "")
    print()
get_pyramid1()
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------

```python
get_pattern_code.get_alpha_triangle_code()
```
### Output of the above code is ;

```python
def get_alpha_triangle(n = 5 , inverted = False) :
    asci = 65
    if inverted == False :
        for i in range(1 , n + 1) :
            for j in range(i) :
                print(chr(asci) , end = "  ")
                asci += 1
                if asci > 90 :
                    asci = 65
            print()
        return
        
    for i in range(n , 0 , -1) :
        for j in range(i) :
            print(chr(asci) , end = "  ")
            asci += 1
            if asci > 90 :
                asci = 65
        print()
get_alpha_triangle()
```

[CLICK HERE FOR CODE'S OUTPUT](https://github.com/Saqibs575/pypatterns-575/blob/main/examples.ipynb)

------------------------------------
------------------------------------

# **Conclusion**
The `pypatterns-575` package simplifies the process of generating and printing patterns in Python. With its versatility, user-friendly interface, and potential educational applications, it's a valuable tool for developers and educators alike. Whether you're visualizing programming concepts or simply exploring your creative side, `pypatterns-575` empowers you to effortlessly create captivating patterns. The inclusion of the pattern_code module further enhances the package's educational value by allowing users to delve into the implementation details of each pattern-generating function.

---------------------------
---------------------------


# **Contributing** <a name = 'contributing'></a>

Contributions to the pypatterns-575 package are welcome! Whether you've found a bug, have suggestions for improvements, or want to add new features, your contributions can make this package even better.

## **How to Contribute**

1. **Open an Issue:** If you come across a bug or have an idea for an improvement, start by opening an issue on the [GitHub repository](https://github.com/Saqibs575/pypatterns-575/issues). Provide as much detail as possible about the issue or suggestion.

2. **Fork the Repository:** If you plan to work on a fix or enhancement, fork the repository by clicking the "Fork" button on the top right of the repository page.

3. **Clone the Fork:** Clone your forked repository to your local machine using the following command, replacing `<your-username>` with your GitHub username:

```sh
git clone https://github.com/<your-username>/pypatterns-575.git
```

## **Create a Branch**:
Before making changes, create a new branch to work on. This helps keep your changes isolated from the main codebase. Use a descriptive branch name related to the feature or bug you're addressing:

```sh
git checkout -b feature/my-new-feature
```

## **Make Changes**: 
Write your code and make the necessary changes. Follow any coding style guidelines and keep the changes focused on a single issue or feature.

## **Test Your Changes**: 
Before submitting a pull request, make sure your changes work as intended and do not introduce new issues. Run tests if available and perform manual testing if needed.

## **Commit and Push**: 
Commit your changes and push them to your forked repository:

```python
git commit -m "Add a descriptive commit message"
git push origin feature/my-new-feature
```

## **Submit a Pull Request**: 
Go to the [original repository](https://github.com/Saqibs575/pypatterns-575) and click the "New Pull Request" button. Select your branch and provide a detailed description of your changes. A team member will review your pull request and provide feedback.

## **Code of Conduct**
Please note that this project follows a Code of Conduct. By participating in this project, you agree to abide by its terms.

Thank you for contributing to the pypatterns-575 package! Your efforts are greatly appreciated.


-------------------------------------
-------------------------------------


# **License** <a name = 'license'></a>

**Copyright &copy; 2023 Saqib Shaikh**

This software package, named "Your Package Name," is distributed under the terms of the GNU General Public License version 3.0 (GPLv3). This license grants you the freedom to use, modify, and distribute this software according to the conditions set forth in the license text.

### License Summary

The GNU General Public License v3.0 (GPLv3) is an open-source license that ensures software remains free and open for all users. It provides the following key permissions and restrictions:

- **Permissions:** You are free to use, share, and modify the software.
- **Copyleft:** Any modified versions of the software must also be distributed under the GPLv3 license terms.
- **Distribution:** If you distribute the software, you must include the source code or a written offer to provide it.
- **Patents:** The license explicitly deals with patents, ensuring users can use the software without concerns about potential patent claims.

### License Text

For the full text of the GNU General Public License v3.0 (GPLv3), please refer to the [LICENSE](https://github.com/Saqibs575/pypatterns-575/blob/main/LICENSE) file located in the repository. This license outlines the complete terms and conditions that apply to this software.

It's important to carefully read and understand the license terms before using or distributing this software.

For any questions or inquiries regarding the license, please contact Saqib Shaikh at saquibs575@gmail.com.

