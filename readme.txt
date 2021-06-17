How to Setup!

################################################################################################

**For linux or mac users :

git clone https://github.com/ayushjaink8/shopon.git             # to clone the git repository

cd shopon                                                       # enter into the project

python -m venv testenv                                          # Creating the virtual environment
. testenv/bin/activate                                          # Activate the virtual environment
[ (testenv) will appear in front of your directory ]

pip install -r requirements.txt                                 # Install the requirements

python manage.py makemigrations
python manage.py migrate

python manage.py runserver                                      # To run the development server

################################################################################################

**For Windows users:

git clone https://github.com/ayushjaink8/shopon.git             # to clone git repository

cd shopon                                                       # enter into the project

python -m venv testenv                                          # Creating the virtual environment
cd testenv/Scripts && activate                                  # Activate the virtual environment
[ (testenv) will appear in front of your directory ]

cd ../../                                                       # to change directory back to shopon
pip install -r requirements.txt                                 # Install the requirements

python manage.py makemigrations
python manage.py migrate

python manage.py runserver                                      # To run the development server

################################################################################################

Note:
1) authentication will not work because client ID and client secret is not there in your db.sqlite3 (django-admin)

2) Just in case .gitignore is not working then use these commands

git rm -r --cached .                             # don't panic it just removed all the files and cache
git add .                                        # added all the files again
git commit -m ".gitignore is working"            # try changing something in .gitignore file now!



