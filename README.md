# Simple Python Progress Bar for Dates

A simple, native, cross-platform python file/module to allow for the easy creation of a countdown clock and colored progress bar between two dates. The file is fairly simple and can be easly modified to count between anything.


### Prerequisites

* Python 3
* *The module makes use of ASNI characters*

### How to Use

To use the Simple Python Progress Bar you can either simply download the progressBar.py file and place it in your python working directory or you can:

**Clone the Git Repo**

```Bash
git clone https://github.com/marcfrankel/GPA_Calculator.git
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
progressBar.create(starting-Datetime-Object, ending-Datetime-Object)
```

The module will then create a progress bar that "hijacks" the program output. The progress bar will release control back to the main thread of the script when it either finishes or the KeyboardInterrupt error is thrown (user press control + c)



## Built With

* [Sublime](https://www.sublimetext.com/) - The editor used
* [Python3](https://www.python.org/) - The Programing language used

## Authors

* **[Marc Frankel](https://marcafrankel.com)** - Head programer

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

