# the-cocktail-app: flask-docker version 
This version requires Docker installed in your machine. Note that it is a flask app so the interaction will be made using a browser.  
If you do not have or do not wish to have Docker nor use Flask, check the other version using native Python or Python in Docker [here](https://github.com/Eldov/the-cocktail-app/blob/main/README.md). 

## Project structure:
```
.
└── flask-docker
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py
    ├── cocktail_app.py
    └── templates
        ├── index.html
        └── exception.html

```
  
In order to run this app, the following steps must be taken:  
  
## **Step 1:**
Having Docker open and running and cloned this repo in your local machine, go to the *flask-docker* folder and run the following comands on your terminal:  
```
docker build -t cocktail-flask .
```
This will use the Dockerfile present in the same folder to create a docker image called *cocktail-flask*.  
Our container will be created based on this image.  
  
## **Step 2:**


Once the image was built, run the following command:  
```
docker run -d -p 5000:5000 --name flask-container1 cocktail-flask
```

This command will make sure the port 5000 is the one being used in the localhost.   
When deploying the application, docker will create the container and keep it running on the background.  

## **Step 3:**

In order to access the web-page, navigate to `http://localhost:5000`.
There, you can insert the desired drink name and submit. The page will show a table with the every drink related to the inserted name. 

The result should be something similar to this:  
![image](https://github.com/Eldov/the-cocktail-app/assets/21317788/7976727d-5df9-4238-9627-e872214991e0)

## **Step 4:**
Ending the application:    
```
docker container stop flask-container1
```  
Deleting the container:  
```
docker container rm flask-container1
```
Deleting the image:  
```
docker image rm cocktail-flask
```
