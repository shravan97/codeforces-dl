import os , sys , argparse , pdfkit , urllib as ul
from bs4 import BeautifulSoup as bs

class CodeForcesDl:
    def __init__(self,contest_id=None , problem=-1 , locale='en' , directory=0):
        if not contest_id:
            raise Exception("Please enter in the contest ID")
        elif type(contest_id)!=int:
            raise Exception("Please enter in a valid contest ID")
        self.contest_id = contest_id
        self.problem = problem
        self.locale = locale
        self.directory = directory

    def get_html(self):
        if self.problem==-1:
            problems_path='problems/'
        else:
            problems_path = 'problem/'+str(self.problem)
        
        contest_path  = 'contest/'+str(self.contest_id)
        locale_path = '?locale='+self.locale
        
        url = "http://codeforces.com/" + contest_path + '/' 
        url = url + problems_path + locale_path 
        # above statement is to reduce characters per line

        page = ul.urlopen(url).read()
        soup = bs(page)

        #Extraction of unwanted elements

        sidebar = soup.find('div',{'id':'sidebar'})
        if sidebar is not None:
            sidebar.extract()

        head_menu = soup.find('div',{'class':'roundbox menu-box'})
        if head_menu is not None:
            head_menu.extract()

        second_level_menu = soup.find('div',{'class':'second-level-menu'})
        if second_level_menu is not None:
            second_level_menu.extract()

        lang_chooser = soup.find('div',{'class':'lang-chooser'})
        if lang_chooser is not None:
            lang_chooser.extract()

        footer = soup.find('div',{'id':'footer'})
        footer.extract()

        if soup.find('div',{'id':'pageContent'}) is not None:
            soup.find('div',{'id':'pageContent'})['style'] = ""\
            "margin-right: 0 !important"

        return str(soup)

    def download_as_pdf(self,out='out.pdf'):
        cwd = os.getcwd()
        files = os.listdir(cwd)
        
        print 'Downloading.....'
        content = self.get_html()

        out_file = out

        if self.directory!=0 and type(self.directory)!=int:
            if self.directory[len(self.directory)-1]!='/':
                self.directory+='/'
            out = self.directory + out
        else:
            self.directory = "this directory"

        try:
            pdfkit.from_string(unicode(content,'utf-8'),out)
        except IOError:
        	raise Exception("Please make sure that you downloaded"\
        	" wkhtmltopdf . \n If not please do it by"\
        	" typing in : \n sudo apt-get install wkhtmltopdf")

        print 'Done !! Checkout '\
        ''+ out_file +' in ' + self.directory + ' !'


def set_options():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('-contest',
    type=int,dest='contest',
    help='contest id (For eg. 681,439 ..etc)')

    arg_parser.add_argument('-problem',
    dest='problem',
    help='problem index (For eg. A,C ..etc)')
    
    arg_parser.add_argument('-lang',
    dest='lang',help=' printing language ')
    
    arg_parser.add_argument('-dir',
    dest='dir',
    help=' path to the directory in which '\
    'the output file has to be saved')

    arg_parser.add_argument('-out',
    dest='out', 
    help=' your desired name for output file')
    
    args = arg_parser.parse_args()
    
    if args.contest==None:
        raise Exception("Please enter a contest id ")
    else:
        c_id = args.contest
        if args.problem==None:
            probs=-1
        else:
            probs=args.problem
        if args.lang==None:
            l='en'
        else:
            l=args.lang
        if args.dir==None:
            directory=0
        else:
            directory=args.dir
        if args.out==None:
            out_file = 'out.pdf'
        else:
            out_file = args.out

        return {'c_id':c_id,'problem':probs,
        'locale':l,'dir':directory,'out':out_file}

def main():
    
    options = set_options()

    dl=CodeForcesDl(options['c_id'] ,
    options['problem'] , options['locale'] 
    , options['dir'])

    dl.download_as_pdf(options['out'])


if __name__=="__main__":
    main()