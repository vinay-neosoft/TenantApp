**Python test**

**Steps to run the application**

**Virtual Environment :**  Create virtual environment using command *virtualenv python_tenant_env*

**Activate Environment :** activate the virtual environment *source python_tenant_env/bin/activate*

**Requirements.** install the requirements in virtual env using *pip install -r docs/requirements.txt*

**Make Migrations** *Python manage.py makemigrations*

**Migrate** *Python manage.py migrate*

**Load Dummy Data** Load dummy data using *python manage.py initdata* .

**Run the Server** *Python manage.py runserver* 

**Demo accounts**

* username - simon, password - password_simon
* username - samson, password - password_samson
* username - christofer, password - password_christofer
* username - margarita, password - password_margarita

* tanant - neosoft  api-key - s3sd521dc5c32csdc65sdc321zcsd65d
* tenant - webwerks api-key - 5as65csdc1sd65321csd65321csd6516

**apis**

* get access token
     * url - /api-token-auth/ 
     * method - POST
     * params - username, password 

* get questions
    * url - /questions
    * method - GET
    * headers - token, api-key
    * params - q (optional)
