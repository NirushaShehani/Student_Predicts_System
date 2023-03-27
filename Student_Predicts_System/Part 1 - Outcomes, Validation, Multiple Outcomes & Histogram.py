# Part 1 - Outcomes, Validation, Multiple Outcomes & Histogram

#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
# Student ID - 20210218
# UOW Number - 19128544

#Create veriables
prog_count = 0
trai_count = 0
modu_count = 0
excl_count = 0

def process(pas, defer, fai):#Main process
    progress_var = ''

    if (pas in range(0, 121, 20) and defer in range(0, 121, 20) and fai in range(0, 121, 20)):

        if (pas + defer + fai) == 120:

            if (pas == 120):
                print('Progress')
                progress_var = 'Progress'
            elif (pas == 100 and (defer == 20 or fai == 20)):
                print('Progress (module trailer)')
                progress_var = 'Progress (module trailer)'
            elif (fai < 80):
                print('module retriever')
                progress_var = 'module retriever'
            elif (fai >= 80):
                print('Excluded')
                progress_var = 'Excluded'

        else:
            print('Total incorrect')

    else:
        print('out of range')

    return progress_var

stf_ver = input('Enter "y" to continue or "q" to exit: ')

while stf_ver != 'q':

    try:
        
#getting inputs
        
        pas = int(input("Enter your total PASS credits: "))
        defer = int(input("Enter your total DEFER credits: "))
        fai = int(input("Enter your total FAIL credits: "))

        progress_var =process(pas, defer, fai)


        if progress_var == 'Progress':
            prog_count = prog_count + 1

        if progress_var == 'Progress (module trailer)':
            trai_count = trai_count + 1

        if progress_var == 'module retriever':
            modu_count = modu_count + 1

        if progress_var == 'Excluded':
            excl_count = excl_count + 1

#catching errors
            
    except ValueError:
        print('Integer Required')

    stf_ver = input('\nWould you like to enter another set of data?Enter "y" for yes or "q" to exit: \n')#getting intupts to quit or to continue


print('Progress  ', prog_count, ' : ', prog_count * '*')
print('Trailer   ', trai_count, ' : ', trai_count * '*')
print('Retriever ', modu_count, ' : ', modu_count * '*')
print('Excluded  ', excl_count, ' : ', excl_count * '*')

print('\n', prog_count + trai_count + modu_count + excl_count, "outcomes in total")

