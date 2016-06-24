Codeforces-dl :inbox_tray: 
-------------------------- 

.. image:: https://travis-ci.org/shravan97/codeforces-dl.svg?branch=master
    :target: https://travis-ci.org/shravan97/codeforces-dl
  
.. image:: https://badge.fury.io/py/codeforces-dl.svg
    :target: https://badge.fury.io/py/codeforces-dl  
    
.. image:: https://landscape.io/github/shravan97/codeforces-dl/master/landscape.svg?style=flat
   :target: https://landscape.io/github/shravan97/codeforces-dl/master
   :alt: Code Health  

Description 
~~~~~~~~~~~ 

| ``Codeforces-dl`` lets you download specific problems/problem sets as
  PDFs from `codeforces.com <http://codeforces.com>`__ for offline practice  
  
   *Inspired by*  `topcoder-dl <https://github.com/tushar-rishav/topcoder-dl>`__

Requirements 
~~~~~~~~~~~~ 

-  `BeautifulSoup4 <https://www.crummy.com/software/BeautifulSoup/>`__

   -  ``$ pip install beautifulsoup4``   **or**
   -  ``$ sudo apt-get install python-beautifulsoup4``

-  `pdfkit <https://pypi.python.org/pypi/pdfkit>`__

   -  ``$ sudo pip install pdfkit``

-  `wkhtmltopdf <http://wkhtmltopdf.org/>`__ (**This dependency has to
   be installed manually**)

   -  ``$ sudo apt-get install wkhtmltopdf``

Installation 
~~~~~~~~~~~~ 

From source : 
''''''''''''' 

.. code:: sh

      git clone https://github.com/shravan97/codeforces-dl.git 

.. code:: sh

      cd codeforces-dl 

.. code:: sh

    python setup.py 

Using pip : 
''''''''''' 

.. code:: sh

        sudo pip install codeforces-dl  

By downloading the Zip/Tar file 
''''''''''''''''''''''''''''''' 

You can also download the zip/tar file from `here <https://github.com/shravan97/codeforces-dl/releases/tag/1.0.0.1>`__ and then unzip the contents to a folder and run  

.. code:: sh

		python setup.py

Usage 
~~~~~ 

.. code:: sh

    usage: codeforcesdl [-h] [-contest CONTEST] [-problem PROBLEM] [-lang LANG]
                           [-dir DIR] [-out OUT]

    optional arguments:
      -h, --help        show this help message and exit
      -contest CONTEST  contest id (For eg. 681,439 ..etc)
      -problem PROBLEM  problem index (For eg. A,C ..etc)
      -lang LANG        printing language
      -dir DIR          path to the directory in which the output file has to be
                        saved
      -out OUT          your desired name for output file  

Sample Usage
~~~~~~~~~~~~ 

.. code:: sh

        codeforcesdl -contest 682 -problem A -dir Demo -out my_fav_problem.pdf  
        

.. code:: sh

        codeforcesdl -contest 678 -dir Demo -out problems.pdf  
        
(Please check `Demo <https://github.com/shravan97/codeforces-dl/blob/master/Demo/>`__ folder for the sample documents)

Contributions 
~~~~~~~~~~~~~ 

Found something useful to contribute to this project ? Please feel free
to give a pull request :smile:

Contributors 
~~~~~~~~~~~~ 

-  `shravan97 <https://github.com/shravan97>`__

License 
~~~~~~~ 

GNU General Public License v3 (GPLv3)