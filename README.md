# Codeforces-dl :inbox_tray: 
## Description
``` Codeforces-dl ``` lets you download specific problems/problem sets as PDFs from [codeforces.com](http://codeforces.com) for offline practice  
> *Inspired by* [topcoder-dl](https://github.com/tushar-rishav/topcoder-dl)  

## Requirements
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)  
    * ``` $ pip install beautifulsoup4 ```  &nbsp; **or**  
    * ``` $ sudo apt-get install python-beautifulsoup4 ```  
- [pdfkit](https://pypi.python.org/pypi/pdfkit)  
    * ``` $ sudo pip install pdfkit ```
- [wkhtmltopdf](http://wkhtmltopdf.org/) (**This dependency has to be installed manually**)  
    * ``` $ sudo apt-get install wkhtmltopdf ```  

## Installation
#### From source :
```sh 
git clone https://github.com/shravan97/codeforces-dl.git 

```  
```sh 
cd codeforces-dl 

```  
```sh 
python setup.py 

```  
## Usage 
```sh 
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

```  
## Sample  
```sh 
codeforces-dl -contest 682 -problem A -dir Demo -out my_fav_problem.pdf 

```  
```sh 
codeforces-dl -contest 678 -dir Demo -out problems.pdf

```  
(Please check [Demo](https://github.com/shravan97/codeforces-dl/blob/master/Demo/) folder for the sample documents)  


## Contributions
Found something useful to contribute to this project ? Please feel free to give a pull request :smile:  

## Contributors  
- [shravan97](https://github.com/shravan97)  

## License
GNU General Public License v3 (GPLv3)  