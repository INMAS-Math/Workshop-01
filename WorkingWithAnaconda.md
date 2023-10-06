# Getting Started with Python and Anaconda
## Introduction
For the INMAS workshops we will be using Python as our primary coding language. Most of the code will be done in jupyter notebooks, which is an open source development environment, that is, a convenient way of organizing our code. With jupyter notebooks, you can run and re-run small blocks of Python code (in any order), so they’re convenient for the work we’ll be doing.

To get started with Python, we recommend that you install [Anaconda](http://anaconda.com), an open-source package manager and Python distribution that includes a suite of useful packages (in addition to basic Python) pre-installed, as well as package management tools. This is an easy way to manage and obtain additional Python packages that you will need in addition to basic Python. For example, it will include matplotlib which will be useful for making plots, and IPython, which will allow you to open, edit, and run the Jupyter notebooks (.ipynb files) which we will be using during the workshop. 

Note: If you already have a preferred Python setup that allows you to run a jupyter notebook, please check that you have an environment compatible with the notebooks we've developed by scrolling to the **Environment** section below. We generally recommend that you use the latest version of Anaconda as many packages might have evolved since the version you have and may not be compatible.

## Installation

In most cases, the installation process for Anaconda will resemble the typical application installation (that is, you download a single linked file, which triggers a graphical installer that you click through). To do this, go to this [link](http://anaconda.com/), and click the download icon
![Download](images/Picture1.png)
which should automatically detect your operating system. Else, you could look for the _Anaconda installers_ box at the bottom of the web page. At the time of this writing, the latest version is Anaconda 23.7.4 or 2023.07.2 using Python 3.11.

![Anaconda Installers](images/Picture2.png)

There will be a few installation steps to click through - you can generally use the defaults. For detailed instructions, here are the particular OS installation guides:

- [Windows](https://docs.anaconda.com/free/anaconda/install/windows/)
- [macOS](https://docs.anaconda.com/free/anaconda/install/mac-os/)
- [Linux](https://docs.anaconda.com/free/anaconda/install/linux/)

## Opening the Navigator

Following a successful installation, you should be able to open and run the "Anaconda navigator" application. This is a launch point for starting jupyter notebooks and other development environments that you may want to use, as well as a place where you can manage your installed python packages.

### Windows Computers

Click on the Windows Icon and search through the applications installed on your computer and open via the Anaconda Icon, which should look like this icon. Alternatively, you can type *anaconda-navigator* in the search tool located in the task bar (notice that, by default, a search is not case sensitive on Windows).

![Anaconda](images/Picture4.png)

### MacOS

Open your Finder and go to the *Applications* Folder, look for *Anaconda-Navigator*, with the same icon you see above.

### Linux

Open a terminal window and type *anaconda-navigator*. Those of you eager to learn Linux in the comfort of your Windows laptop should consider running the *Windows Subsystem for Linux* (WSL) available for free. This will allow you to run a full version of Linux (e.g., Ubuntu) within your Windows operating system. Really cool. More info [here](https://learn.microsoft.com/en-us/windows/wsl/install).

Upon successfully opening the navigator you should see something resembling the following window. Be patient, it sometimes takes a while to load.

![Navigator](images/Picture5.png)

The navigator can be used to start many applications. Those of interest to us are mainly the jupyter notebook and a terminal shell. The advantage of starting a command shell from the navigator is that all the environment variables are already pre-configured for Python. On Windows, we recommend using the PowerShell Prompt over CMD, as the former provides command line editing and history and is therefore more user friendly.

## Testing your anaconda installation

First start a terminal shell from the Anaconda Navigator or otherwise. Then type

`conda info`

and make sure that the version is 23.7.4 with Python being 3.11.4.final. The command

`conda list`

will list all the packages installed on your computer and their version numbers. Notice that the packages contain matplotlib, numpy, pandas, and seaborn packages that we will learn about and use during the training. A successful installation should have a large number of packages available (including those mentioned) and should have the proper versions listed above.

## Environment and Upgrade

If you already have a version of Anaconda installed, make sure that you have an environment that is compatable with the INMAS workbooks. Anaconda supports multiple "virtual environments," that is, you can have multiple sets of packages with different versions installed. This can be helpful when you need different version packages for different projects that might not be compatable with one another. Instructions on creating and managing new environments can be found [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). 

Note that the standard Anaconda install should come with all the packages needed for INMAS pre-installed. For workshop 1, please make sure that you have a very recent version of the following:
- numpy
- scipy
- jupyter
- matplotlib
- seaborn
- pandas

Note that for too complicated a set of packages it is possible that Anaconda will break. Every once in a while I end up upgrading to the latest version doing a complete uninstall and reinstall of Anaconda. Instructions on uninstalling Anaconda can be found [here](https://docs.anaconda.com/free/anaconda/install/uninstall/). To uninstall anaconda On Windows, uninstall the Anaconda application. On mac and Linux you can use anaconda-clean, or (not recommended) delete the entire *anaconda3* directory located in you home directory before proceeding with a fresh install.

Checking the version of Anaconda and Python is relatively simple. Open a terminal window (anaconda Prompt on Windows, Terminal on Mac and Linux – more details below) and just type:

`conda info`

You should then get something like this:

![Conda info](images/Picture3.png)

Make sure that the versions of both Python and *conda* match the version described above and in this window.

---

## Appendix: Navigating using a command shell

It is sometimes easier to use command line interface over a graphical user interface. Starting a terminal can be done through the Anaconda Navigator, or through starting a terminal on Mac or Linux. Navigating files and directories consists of using the following five basic commands:

- `ls` or `dir` list files in current directory
- `cd` change current directory
- `pwd` print working directory
- `mkdir` make a new directory
- `rmdir` remove a directory

Note that when navigating, '.' means the current directory, and '..' means the parent directory. Therefore,

`cd .`

is a null operator, while

`cd ..`

moves to the parent directory. Please take a moment to navigate around the directory tree of your computer and familiarize yourself with these commands.

Help on any of these commands can be obtained by typing, for the command `ls`, for example,

`man ls`

where man stands for manual.

Files can be copied (`cp`), moved (`mv`), or deleted (`rm`). Use `man` to get more information on these commands. Be cautious with the `rm` command as it does not ask for a confirmation of the deletion by default.

Using a command line interface is often the preferred method for navigating directories, or projects with multiple files, especially when one is using a version control system such as `git`.
