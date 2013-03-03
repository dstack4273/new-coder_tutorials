---
layout: post.html
title: "Part 2: Database Setup"
tags: [scrape]
---

Walkthrough of scraping a webpage and saving it to a database.


### Create a Database

Our initial step needs to create the database that we plan to use to save all of our crawled data.

To do that, we will start a Postgres shell on localhost:

```bash
(ScrapProj)$ psql -h localhost
psql (9.1.4, server 9.1.3)
Type "help" for help.

newcoder=#
```
The `newcoder=#` is the PostGres prompt. We simply create a database with this command:

```psql
newcoder=# create database scrape;
```

Notice I had to include the semicolon there.  This is pretty much all the raw SQL code we're going to touch. If you are curious, you can learn more on how to interact with PostGres in their [docs](http://www.postgresql.org/docs/9.2/static/index.html).

### Settings.py

Our `settings.py` file only has 5 variables defined (pop quiz: these variables are all caps, do you remember why? Refer to the Data Viz tutorial for a refresher).

For right now, we'll only address the `DATABASE` variable 
