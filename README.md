# concert_analytics

# concert_analytics

Selenium webdriver to scrape vividseats concerts website. Geared the spider to collect key attributes (time, artist, venue, artist popularity, genre of music, day of the week) of every concert in Los Angeles, New York, Denver, Boston, Chicago, and Dallas and the price of tickets 2 months before, 2 weeks before, and 2 days before the concert. using AWS Lambda to schedule the spider to run every day and send the data to MongoDB to store. Working on a Machine Learning model using feature engineered fields to find casualities in ticket price surges so that the model can then predict undervalued concert tickets to buy and sell for profit.
