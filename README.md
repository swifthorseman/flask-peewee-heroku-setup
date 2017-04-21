# Deploying the app to Heroku and provisioning a database

## Pre-requisites

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
1. Optionally, install [psql](https://devcenter.heroku.com/articles/heroku-postgresql#pg-psql) if you want to connect to the Postgres
database on Heroku from the command line.


## Steps

### Deploying the app

1. Clone this repository:
    ```shell
    $ git clone git@github.com:swifthorseman/flask-peewee-heroku-setup.git
    ```
1. Create the app on Heroku and deploy it:
   ```shell
   $ heroku login
   $ heroku create
   $ git push heroku master
   ```

Running `heroku create` will generate the name and the URL from which it can be accessed.

### Setting up a new database

1. Create a new database on Heroku as an add-on to the app:
   ```shell
   $ heroku addons:create heroku-postgresql:hobby-dev
   ```
   Verify that the database has been created by running:
   ```shell
   $ heroku pg:info
   ```
1. Set up a config variable:
   ```shell
   $ heroku config:set HEROKU=1
   ```
1. Verify that the required environment variables are set:
   ```shell
   $ heroku config
   ```
   The values for both `DATABASE_URL` and `HEROKU` should be set.

### Creating a table on the database

1. Launch a shell on Heroku:
   ```shell
   $ heroku run bash
   ```
1. Run:
   ```shell
   $ python tellytubbies.py
   ```
1. From a local shell, verify that the table was created successfully:
   ```shell
   $ heroku pg:info
   ```
   The command should output the number tables (1) and the number of rows (4).

1. Use `pgsql` to connect to the database and query the tables:

```
   $ heroku pg:psql

   ::DATABASE=> \dt
             List of relations
 Schema |    Name    | Type  |     Owner
--------+------------+-------+----------------
 public | tellytubby | table | sgaluyzmzkklpj
(1 row)
::DATABASE=> select * from tellytubby;
 id |    name     | colour
----+-------------+--------
  1 | Tinky Winky | Purple
  2 | Dipsy       | Green
  3 | Laa-Laa     | Yellow
  4 | Po          | Red
(4 rows)
```

Connecting to the app through the URL (which was generated when `heroku create` was run) will retrieve entries from the database and display them in the browser.
