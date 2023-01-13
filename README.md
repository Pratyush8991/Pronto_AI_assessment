# Pronto_AI_assessment
Take home assessment for ProntoAI

### Question

Your task is to create a program that prints specific facts about a local git repository. You can use any language, and you are welcome to import existing packages.

Your program should take in one argument:
git_dir: directory in which to assess git status

Your program should print the following things:
active branch (boolean)
whether repository files have been modified (boolean)
whether the current head commit was authored in the last week (boolean)
whether the current head commit was authored by Rufus (boolean)


### Solution
I have solved the above assessment using Python. You will need the <b>gitpython</b> package to run the program. (pip install gitpython).
The program takes the directory of a local git repository as an argument, and opens it using the 'gitpython' package. The head commit and the active branch are assigned to variables <b>'head_commit'</b> and <b>'branch'</b> respectively. 
1. Using the package's inbuilt method <b>'is_active()'</b>, we find the active branch. 
2. Using the package's inbuilt method <b>'is_dirty()'</b> we find if there have been any changes to the branch.
3. Using the 'datetime' package, we calculate the difference between 'now' and the 'authored_datetime' - which indicates when the repository was created. This is then evaluated against a time delta of 1 week. If it is less than that, it assigns True to the variable <b>last_week</b>.
4. We then use <b>'author.name'</b> on head_commit to get the name of the author and check its equality to "Rufus". If it is True, it assigns True to the variable <b>'authored_by_rufus'</b>, else False.  
Finally, we print out all the variables values.

### Running the script
You can run this script from the command line by providing the directory of the local git repository as an argument, for example: 
<b>python prontoAI.py /path/to/local/git/repository</b>
