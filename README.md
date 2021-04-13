# Project Manager REST API

This API allows you to organize projects and their tasks. You can create, delete, update, get projects, all of this operations can also performed over theirs tasks. 

This API implements [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) (JSON WEB TOKEN) that's why you must be first registered and after logged in order to get a Token that allows you to do request to API.


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

#### Look at this example:

Open postman client and type `http://127.0.0.1:5000/api/v1/users/signup`. Add the information of the user to register in the body, `username`, `email` and `password`. Choose `POST` method.

See the picture

<a href="https://imgur.com/7yWbcfk"><img src="https://i.imgur.com/7yWbcfk.png" title="source: imgur.com" /></a>

Once the information has been added you can make the post request, if everything was OK the response will be `Successfully registered.` and now you can login with this user to have access to other end point.

To loggin you must change the endpoint above to `http://127.0.0.1:5000/api/v1/users/login.` and send in the body the `username` and `password` of the user prevously registered.

Like so:

<a href="https://imgur.com/ag9gmia"><img src="https://i.imgur.com/ag9gmia.png" title="source: imgur.com" /></a>

If it went well, the response will be a `token`. This token will be needed to make any another request.

> This token has expiration time of 5 minutes, this means that you must login each 5 minutes to get other token and be able to interact with the API

<a href="https://imgur.com/uaSpeMW"><img src="https://i.imgur.com/uaSpeMW.png" title="source: imgur.com" /></a>

For example, you could make a get request to following endpoint to see all of the projects. For this you must placed in the header the token recieved at moment of loggin: Look at the picture:

<a href="https://imgur.com/mx9L8Wb"><img src="https://i.imgur.com/mx9L8Wb.png" title="source: imgur.com" /></a>

Every time you want to access to any end point you must performe the same proccess.

In order to know more about the endpoints of the API you can read the documentation.

## Support

If you have any problem executing this AP, please do not hesitate to contact me at [Twitter](https://twitter.com/aarizatr)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

#### Andres Ariza-Triana 
