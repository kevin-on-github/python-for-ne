# python-for-ne
 - Project files for 'Python Network Programming for Network Engineers (Python 3)'.
 - David Bombil Class https://www.udemy.com/course/python-network-programming-for-network-engineers-python-3
 - First project chapter is 3. Each project has it's own directory and lab files.

 NOTE: Certain portions of this lab require loading several python modules. Check the requirements.txt file for the complete
       loadout.
       Also see the cisco-fix.txt file for resolving the ssh issues for adding support for outdated CML images.

 NOTE: Chapter 9 introduces python module simple-crypt which installs a requirement pycrypto which appears to be
       outdated. I had to manually remove pycrypto and install pycryptodome. Docs for simple-crypt mention the dependencie
       was updated, but alas this caused time.clock errors in the scripts.
        - pip uninstall pycrypto
        - pip install pycryptodome
 - From CH10-13 is pure lecture with simple python text processing. It's not meaty enough to lab, but is well worth the time I spent doing it.
 - In 14 I start to implement some of the work done over the previous chapters with more in depth text processing. Though not mentioned I leaned in with sqlite3, jinja2, and how to read data from sql, process text through a jinja2 template. Things are starting to come together. Slow progress, but progress nonetheless.
