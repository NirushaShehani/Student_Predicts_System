# Part 2 - Vertical Histogram (extension)


#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID - 20210218
#UOW Number - 19128544

#Creating veriables
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
                print('Do not progress-module retriever')
                progress_var = 'Do not progress-module retriever'
            elif (fai >= 80):
                print('Excluded')
                progress_var = 'Excluded'

        else:
            print('total incorrect')


    else:
        print('Range error')

    return progress_var

stf_ver = input('Enter "y" to continue or "q" to exit: ')#getting inputs to quit or to continue

while stf_ver != 'q':

    try:

        pas = int(input("Enter your total PASS credits: "))
        defer = int(input("Enter your total DEFER credits: "))
        fai = int(input("Enter your total FAIL credits: "))

        progress_var = process(pas, defer, fai)

        if progress_var == 'Progress':
            prog_count = prog_count + 1

        if progress_var == 'Progress (module trailer)':
            trai_count = trai_count + 1

        if progress_var == 'Do not progress-module retriever':
            modu_count = modu_count + 1

        if progress_var == 'Excluded':
            excl_count = excl_count + 1
#catching errors
    except ValueError:
        print('Integer Required')

    stf_ver = input('\nWould you like to enter another set of data?Enter "y" for yes or "q" to exit:\n')#getting inputs to quit or to continue

print("     progress |", "Trailer |", "Retriever |", "Exclude")#Histogram

for i in range(max(prog_count, trai_count, modu_count, excl_count)):

    if (i < prog_count):
        print("\t*", end=' ')
    else:
        print("\t ", end=' ')

    if (i < trai_count):
        print("\t  *", end=' ')
    else:
        print("\t ", end=' ')

    if (i < modu_count):
        print("\t    *", end=' ')
    else:
        print("\t ", end=' ')

    if (i < excl_count):
        print("\t      *", end=' ')
    else:
        print("\t ", end=' ')

    print()
print('\n', prog_count + trai_count + modu_count + excl_count, "outcomes in total")
