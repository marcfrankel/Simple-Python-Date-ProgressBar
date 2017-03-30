# Simple Python Progress Bar for Dates V 1.1

A simple, native, cross-platform python file/module to allow for the easy creation of a countdown clock and colored progress bar between two dates. The file is fairly simple and can be easly modified to count between anything.


### Prerequisites

* Python 3
* *The module makes use of ASNI characters*

### How to Use

To use the Simple Python Progress Bar you can either simply download the [progressBar.py](https://raw.githubusercontent.com/marcfrankel/Simple-Python-Date-ProgressBar/master/progressBar.py) file and place it in your python working directory or you can:

**Clone the Git Repo**

```Bash
git clone https://github.com/marcfrankel/Simple-Python-Date-ProgressBar.git
```
Then also move the progressBar.py file into your python working directory

**Importing**

If the progressBar.py file is in the proper place you should be able to import the module with the following import statement at the top of your file

```Python
import progressBar
```
**Creation**

To create a progressBar in your code call progressBar.create() and pass in two [datetime](https://docs.python.org/3/library/datetime.html) objects

```Python
response = progressBar.create(starting-Datetime-Object, ending-Datetime-Object)
```

The module will then create a progress bar that "hijacks" the program output. The progress bar will release control back to the main thread of the script when it either finishes or the KeyboardInterrupt error is thrown (user press control + c). To know the reason the progress bar stoped please see below.

**Responses**

the variable 'response' from above can be the following three ints and it is up to you how to handle them:

```
0 = The end date is before the start date. (No coutdown displayed)
1 = The countdown finished
2 = The user pressed control+c 
```

## Built With

* [Sublime](https://www.sublimetext.com/) - The editor used
* [Python3](https://www.python.org/) - The Programing language used

## Authors

* **[Marc Frankel](https://marcafrankel.com)** - Head programer

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

