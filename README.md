# Project Manager REST API

This API allows you to organize projects and their tasks. You can create, delete, update, get projects, all of this operations can also performed over theirs tasks. 

This API implements JWT (JSON WEB TOKEN) that's why you must be first registered and after logged in order to get a Token that allows you to do request to API.


## Installation

In order to start using this API you must install `Python 3.8.5` and `MySQL 5.7`. (These were the versions used in develop).

Now, follow this steps:

1. Choose a place in your computer and clone this repository. Type in your terminal:
```
$ git clone https://github.com/aarizat/project_manager-REST_API.git
```
2. Once the repository has been downloaded, enter to it and create a python virtual enviroment. (This step is not required but it is highly recomended).
```
$ cd project_manager-REST_API
$ python3 -m venv env
```
The above command will create a folder called `env`.
> Make suere to use the right Python version at time of creating the virtual enviroment.
3. Install the requirements needed to run the API.
```
$ pip install -r requirements.txt
```
4. Configure the database.

This API uses a MySQL database, the reason why you must configure one. For this it's included in this repository a file called `setup_db.sql` which will help you to do it easily. So in your terminal type:
```
$ cat setup_db.sql | mysql -uroot -p
```
Once you run the above command you must enter the passoword and wether all of it was OK the database should be created.
> You can change database name, username and password, to do so, modify the `setup_db.sql` file before runnig the above command.

5. Configure enviroment variables. The following variables will be used to run the API
```
API_HOST   ----> IP where the API is hosted.
API_PORT   ----> port where the api will be listening to.
DB_NAME    ----> database name
DB_USER    ----> username who has permisions over the database
DB_PWD     ----> database password
DB_HOST    ----> IP where the database is hosted.
SECRET_KEY ----> key used by Flask to proccess the incriptation.
```

## Usage

After setup proccess above the API is ready to be executed. In order to do it you only to need to execute below command in your terminal:
```
$ API_HOST=0.0.0.0 API_PORT=5000 DB_USER=user_db DB_PWD=pwd_db DB_HOST=localhost DB_NAME=projects_db SECRET_KEY='gues me!' python -m api.v1.app
```
> Change the enviroment variables if you modified the `setup_db.sql` file.

Now, the API is running in the 5000 port ready to receive requests. For this is good a idea to use a client like `Postman`.



