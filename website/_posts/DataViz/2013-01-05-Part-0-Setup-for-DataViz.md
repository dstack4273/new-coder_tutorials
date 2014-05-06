---
layout: post.html
title: "Part 0: Setup"
tags: [DataViz]
url: "/dataviz/part-0/"
---

Initial setup for our Data Visualization Tutorial.


### Setup

**IMPORTANT**: Please be sure to work through the [machine setup]({{ get_url("begin/setup-your-machine")}}) before proceeding.

* Change into the Data Viz project:

```bash
$ cd new-coder/dataviz
```
* Make sure you’ve installed [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from Initial Requirements to set up your terminal correctly.  More information can be find at virtualenvwrapper’s [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* To make a virtual environment specific to your Data Viz project, run the following command. You should see `(DataVizProj)` before your prompt.

```bash
$ mkvirtualenv DataVizProj
(DataVizProj)$
```
* Now we will install the package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

```bash
(DataVizProj) $ pip install -r requirements.txt
```
* **NOTE** Sometimes, NumPy is finicky. If the previous step returns errors, try:

```bash
(DataVizProj)$ pip install numpy
(DataVizProj)$ pip install matplotlib
(DataVizProj)$ pip install geojson
```

* **NOTE** Sometimes, matplotlib is finicky as well. If you are on a Mac and "pip install matplotlib" did not work, you are probably missing the supporting packages freetype2 and libpng. Windows users do not need to worry about this as these packages are already included in the standard matplotlib Windows installers. For Mac users, below are detailed instructions on how to install them. 
Note that libpng has a dependency on zlib library, so we have to install that first. So in total we install 3 supporting packages: 

   **1. ZLIB**
   Go to http://www.zlib.net/ and download the latest source code archive.
   Scroll down to zlib source code, and download version 1.2.7, tar.gz format
   Unpack the zip file
   Open a Terminal window, cd to the zlib source folder, and configure, make, and install the library as follows:
   
```bash
$ cd ~/Downloads
$ cd zlib-1.2.7
$ ./configure
$ make
$ sudo make install
```

   **2. LIBPNG**
   Go to http://www.libpng.org/pub/png/libpng.html and download the latest source code archive
   Scroll down and download by clicking the "tar.gz" link on the download.sourceforge.net row
   Unpack the zip file
   Open a Terminal window and type:

```bash
$ cd ~/Downloads
$ cd libpng-1.5.14
$ ./configure
$ make
$ make check
$ sudo make install
```

   **3. FREETYPE**
   Go to http://sourceforge.net/projects/freetype/files/latest/download?source=files and the download of the source file should shart automatically
   Unpack the zip file
   Open a Terminal window and type:

```bash
$ cd ~/Downloads
$ cd freetype-2.4.11
$ ./configure
$ make
$ sudo make install
```

After installing these three packages, type "pip install matplotlib" again and it should work. 


* Test the installation real quick by starting up the Python interpreter:

```bash
(DataVizProj)$ python
>>> import numpy
>>> import matplotlib
>>> import geojson
```
* If you have no errors (you would just see the `>>>` prompt), then you’re good to go. You can close out of the Python interpreter by pressing `CTRL+D`. If you do have errors, I’d try downloading [numpy](http://scipy.org/Download) and [matplotlib](http://matplotlib.org/downloads.html) manually.


[Continue on to Part 1: Parsing our Data &rarr;]( {{ get_url("/dataviz/part-1/")}})
