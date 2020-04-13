# Daily Scrum Discord Bot

This project is ready for deployment in heroku, you just need to add your
application's token and a role name to the environment variables.

It will only consider for the daily those members who belongs to the role
specified in the 'ROLE' environment varibale, if not specified it will take
the role 'daily participant' by default.


### Deployment

```sh
$ heroku apps:create <YOUR_APP_NAME>
$ git push -u origin master
```
