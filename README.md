# Gramener-assignment

## Task One Explanation:

- clone repository using git i.e., `git clone https://github.com/RaiVaibhav/gramener-assignment.git`
- Run `cd assignment`.
- Run python script using command - `python3 taskone.py`
- Python 3.5 standard library as os.scandir() has been used for better performance.
- logic was to first iterate through all the path inside the given directory and after that check
  that whether it is file or a directory if it's a file append the file path to the list and if its a directory then recurse the above process and get the file path from subdirectories and in last print the
  list.

## Task Two Explanation:

### How to run

- Create a postgres sql database.
- run `pip3 install -r requirements.txt`
- Run `python manage.py makemigrations` and `python manage.py migrate`.
- Run `python manage.py runserver` to run the server.

Don't forgot to initially create a `virtualenv`.

### Logic:

- Created a Student app using - `python manage.py startapp student`.
- A Student Model created to create a table data in the database
- A Student Form using Student model created to get the data from the html template
  and enter it in the postgres database using `new_student` view.
- A `students_detail` created to render all the Student detail in form of table on the html tempate.
- Deployed on herokuapp - https://gramener-assignment.herokuapp.com/

## Task Three Explanation:

- clone repository using git i.e., `git clone https://github.com/RaiVaibhav/gramener-assignment.git`
- Run `cd assignment`.
- Run python script using command - `python3 taskthree.py`
- List converted to set using type conversion.
- Set intersection property is used to get the common elements in both the set and converted back
  to list using type conversion.
- Set subtraction property is used to get the elements only in l1 not in l2.

