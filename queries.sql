--count of records
select count(*) from ecommerce;

--unique brand names
select distinct brand from ecommerce;

--all records of amazon brand
select * from ecommerce where brand='Amazon';

--Records having prod_review has 'good'
select * from ecommerce where reviews_text like '%good%';

--records under electronic category
select * from ecommerce where categories like '%Electronics%';

select * from ecommerce where PrimaryCategories ='Electronics' and brand='Flipkart';

--summary
select primaryCategories, sum(case when sentiment = 'positive' then 1 else 0 end) as positive_count, 
sum(case when sentiment = 'negative' then 1 else 0 end) as negative_count
from ecommerce
group by primaryCategories;

--positive sentiment
select * from ecommerce where sentiment = 'positive';

select brand, 
 sum(case when sentiment='positive' then 1 else 0 end) as positive_sentiment_count,
 sum(case when sentiment='negative' then 1 else 0 end) as negative_sentiment_count,
 count(*) as total_reviews,
 round(sum(case when sentiment='positive' then 1 else 0 end) / count(*) * 100, 2) as positive_percentage,
 round(sum(case when sentiment='negative' then 1 else 0 end) / count(*) * 100, 2) as negative_percentage
 from ecommerce
 group by brand;
 
select count(*) as product_count,
primaryCategories from ecommerce
group by primaryCategories;

--all records from the 'ecommerce' table where the product name contains the word 'Tablet' as a substring
select * from ecommerce
where name like '%Tablet%';

select count(*) as review_count
from ecommerce where reviews_text like '%Alexa%';