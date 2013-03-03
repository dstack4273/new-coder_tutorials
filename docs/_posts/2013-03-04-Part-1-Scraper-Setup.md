---
layout: post.html
title: "Part 1: Scraper Setup"
tags: [scrape]
---

Walkthrough of building the scraper setup portion of the tutorial.

### Define our Items

**TODO** When the dir struct is all fixed, add Module location

In our `items.py` file, scrapy needs us to define containers for the data that we plan to scrape. If you have worked through the Django [tutorial](https://docs.djangoproject.com/en/1.5/intro/tutorial01/) at one point, you'll see that the `items.py` is similar to `models.py` in Django.

First, using scrapy's item module, we import `Item` and `Field:

```python
from scrapy.item import Item, Field
```

Simple enough. Now we'll create a class, and name it after the kind of data that we'll scrape, `LivingSocialDeal`:

```python
class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
```

For our `LivingSocialDeal` class, we inherit from `Item` - which basically takes come pre-defined objects that scrapy has already built for us.

**A note about inheritance:** You can think of class inheritance like the birds and the bees. For instance, we can have a base class, `class Human(object)`, that will have some human attributes - like a function for running, for bathing, eating, etc.  Then we can inherit from the `Human` class to make a new class, `class Superwoman(Human)`. Because we inherit from `Human`, we can still access the running, eating, bathing functions. But - perhaps Superwoman runs _faster_ than the average human, so we can _redefine_ the running function. This basically rewrites over Human's running function.  We can also add a flying function, of which the `Human` class will not have.  So, when we want a new human, we simply just instantiate it by assigning the class to a variable: `my_new_human = Human()`. And when we want a Superwoman: `my_superwoman = Superwoman()`.

Back to the tutorial - let's add some items that we actually want to collect. We assign them to `Field()` because that is how we specify metadata to scrapy:

```python
class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = Field()
    description = Field()
    link = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()
```

Nothing too hard - that was it. In scrapy, there are no other field types, unlike Django. So, we're sort of stuck with `Field()` :)

Let's play around with this in the Python terminal. Make sure your `ScrapeProj` virtualenv is activated.

```bash
>>> from scrapy.item import Item, Field
>>> from items import LivingSocialDeal
>>> deal = LivingSocialDeal(title="$20 off yoga classes", category="health")
>>> print deal
LivingSocialDeal(title='$20 off yoga classes', category='health')
>>> deal['title']
'$20 off yoga classes'
>>> deal.get('title')
'$20 off yoga classes'
>>> deal['category']
'health'
>>> deal['location'] = "New York"
>>> deal['location']
'New York'
```

The scrapy `Item` class behaves very similar to Python's dictionaries with the ability to get keys and values.

Now that it's all setup, let's [setup our spider &rarr;]({{ get_url('Part-2-Writing-our-Spider')}})