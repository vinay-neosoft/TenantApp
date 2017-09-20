**Tenants Application**

**Steps to run the application**

**Set up Virtual Environment**  

Check whether virtualenv is installed. If virtualenv is not installed then install virtualenv using command *pip install virtualenv*

After installing virtualenv, create virtual environment using command *virtualenv python_tenant_env*

**Activate Virtual Environment** 

To activate the virtual environment, you need to change directory to python_tenant_env/bin using command *cd python_tenant_env/bin*

After changing directory, activate virtual environment using command *source activate*

**Install Packages** 

Make sure virtual environment is activated before installing packages.
Install the packages in virtual environment using *pip install -r docs/requirements.txt*

**Make Migrations** 

After installing all the packages successfully, Create migration using command *Python manage.py makemigrations*

**Migrate** 

After successfull execution of above command, run the migrate command using *Python manage.py migrate*

**Load Dummy Data** 

After all the above steps are successfully executed then Load dummy data using *python manage.py initdata*.

**Run the Server** 

To start the server, use command *Python manage.py runserver* 

**Demo accounts data**

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
    * url - /api/questions
    * method - GET
    * headers - token, api-key
    * params - q (optional)
