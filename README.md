# Setup instructions for the project.

- The instructions to setup project
- Fork the repo to your github account
- software need for this project **Postgres, python**
  
```bash
 git clone https://github.com/user-name/Sarva_Suvidhan_assignment
 cd kpa_app
 python3 venv .vevnv
 source ./.vemv/Scrips/activate

 python3 install -r requirements.txt
```
- create kapa_db in posgres dbms
- now run the following command to run

```py 
    python manage.py makemigrations
    python manage.py migrations
    python manage.py runserver
```
## The technologies and tech stack used.

- django templates
- Django model forms
- html

## A list and description of the implemented APIs.

- created CURD of **Bogie checksheet** api with creation, updation, delete and display
  
## Any limitations or assumptions made.
- it works in django app need to modify the code inorder to integrate to frontend.