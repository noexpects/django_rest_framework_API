## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count.

## **Steps to run project with Docker:**

- Clone this repository.
- Open CMD in project's folder
- Run next commands:
    1. docker-compose build
    2. docker-compose up
    3. docker-compose exec web python manage.py migrate
    4. docker-compose exec web python manage.py createsuperuser
## **Some links:**

- [Project deployed on Heroku](https://drfapitesttask.herokuapp.com/api/v1/posts/)
- [Postman collection](https://go.postman.co/workspace/My-Workspace~a6d0930c-7408-45c8-873a-9cf15863e4e6/collection/18640363-361f2004-bb00-4a84-acc3-6a49d65fb16c)
- [Postman Enviroment for deployed project](https://go.postman.co/workspace/My-Workspace~a6d0930c-7408-45c8-873a-9cf15863e4e6/environment/18640363-215c18d4-cb84-4e4e-9ad9-6092e486aab7)
- [Postman Enviroment for local testing](https://go.postman.co/workspace/My-Workspace~a6d0930c-7408-45c8-873a-9cf15863e4e6/environment/18640363-110c8fb3-7679-4c1a-a5b2-4d420267c317)

#### P.S.
Resseting posts upvotes counter perfomed with free Heroku Scheduler add-on. 
It runs custom management command once a day at 12:00 AM.

If you want to reset the upvote counter of all posts locally, run the following command:
'python manage.py reset_upvotes'
