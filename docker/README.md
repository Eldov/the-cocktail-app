# the-cocktail-app: docker version 
This version requires Docker installed in your machine.  
If you do not have or do not wish to have Docker, check the other version using native Python [here](https://github.com/Eldov/the-cocktail-app/blob/main/README.md).  
  
In order to run this app, the following steps must be taken:  
  
## **Step 1:**
Having Docker open and running and cloned this repo in your local machine, go to the *docker* folder and run the following comands on your terminal:  
```
docker build -t cocktail-python .
```
This will use the Dockerfile present in the same folder to create a docker image called *cocktail-python*.  
Our container will be created based on this image.  
  
## **Step 2:**


Once the image was built, run the following command:  
```
docker run -it --name python-container1 cocktail-python
```

This command will create the container and take you immediately to the python application inside the container.  
Just as in the venv version, you will receive the message *Enter your drink:*  
Insert the desired drink name and you will receive a json as the following:  

```json  
{
   "Id": {
      "0": "13196",
      "1": "16967",
      "2": "178362",
      "3": "178363",
      "4": "178364",
      "5": "12800",
      "6": "14167",
      "7": "15403",
      "8": "12460"
   },
   "Name": {
      "0": "Long vodka",
      "1": "Vodka Fizz",
      "2": "Vodka Slime",
      "3": "Vodka Lemon",
      "4": "Vodka Tonic",
      "5": "Coffee-Vodka",
      "6": "Vodka Martini",
      "7": "Vodka Russian",
      "8": "Vodka And Tonic"
   },
   "Category": {
      "0": "Ordinary Drink",
      "1": "Other / Unknown",
      "2": "Cocktail",
      "3": "Cocktail",
      "4": "Cocktail",
      "5": "Homemade Liqueur",
      "6": "Ordinary Drink",
      "7": "Ordinary Drink",
      "8": "Ordinary Drink"
   },
   "Alcoholic": {
      "0": "Alcoholic",
      "1": "Alcoholic",
      "2": "Alcoholic",
      "3": "Alcoholic",
      "4": "Alcoholic",
      "5": "Alcoholic",
      "6": "Alcoholic",
      "7": "Alcoholic",
      "8": "Alcoholic"
   },
   "Glass": {
      "0": "Highball glass",
      "1": "White wine glass",
      "2": "Highball glass",
      "3": "Highball glass",
      "4": "Highball glass",
      "5": "Collins Glass",
      "6": "Cocktail glass",
      "7": "Collins Glass",
      "8": "Highball glass"
   },
   "Instructions": {
      "0": "Shake a tall glass with ice cubes and Angostura, coating the inside of the glass. Por the vodka onto this, add 1 slice of lime and squeeze juice out of remainder, mix with tonic, stir and voila you have a Long Vodka",
      "1": "Blend all ingredients, save nutmeg. Pour into large white wine glass and sprinkle nutmeg on top.",
      "2": "Fill glass with ice. Add vodka, 7-up then finish with the lime juice.",
      "3": "The vodka lemon is prepared directly in a highball glass or in a large tumbler: put 6-7 ice cubes in the glass, pour the vodka, lemonade and mix with a bar spoon. Finally decorate with a slice of lemon and, if you prefer, add a few mint leaves. Your vodka lemon is ready to be served.",
      "4": "Wash and cut 1 wedge and 1 slice of lime or lemon.\r\nFill a tumbler with fresh ice.\r\nPour the desired dose of vodka and top up with the tonic.\r\nSqueeze the lime wedge into the glass and decorate with the slice.\r\nThat's all, very simple: it's just the recipe for happiness!",
      "5": "Boil water and sugar until dissolved. Turn off heat. Slowly add dry instant coffee and continue stirring. Add a chopped vanilla bean to the vodka, then combine the cooled sugar syrup and coffee solution with the vodka. Cover tightly and shake vigorously each day for 3 weeks. Strain and filter. Its also best to let the sugar mixture cool completely so the vodka won't evaporate when its added. If you like a smoother feel to the liqueur you can add about 1 teaspoon of glycerine to the finished product.",
      "6": "Shake the vodka and vermouth together with a number of ice cubes, strain into a cocktail glass, add the olive and serve.",
      "7": "Mix it as a ordinary drink .",
      "8": "Pour vodka into a highball glass over ice cubes. Fill with tonic water, stir, and serve."
   },
   "Thumbnail": {
      "0": "https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg",
      "1": "https://www.thecocktaildb.com/images/media/drink/xwxyux1441254243.jpg",
      "2": "https://www.thecocktaildb.com/images/media/drink/apex461643588115.jpg",
      "3": "https://www.thecocktaildb.com/images/media/drink/mql55h1643820632.jpg",
      "4": "https://www.thecocktaildb.com/images/media/drink/9koz3f1643821062.jpg",
      "5": "https://www.thecocktaildb.com/images/media/drink/qvrrvu1472667494.jpg",
      "6": "https://www.thecocktaildb.com/images/media/drink/qyxrqw1439906528.jpg",
      "7": "https://www.thecocktaildb.com/images/media/drink/rpttur1454515129.jpg",
      "8": "https://www.thecocktaildb.com/images/media/drink/lmj2yt1504820500.jpg"
   },
   "Date Modified": {
      "0": "2017-08-24 10:00:12",
      "1": "2015-09-03 05:24:03",
      "2": null,
      "3": null,
      "4": null,
      "5": "2016-08-31 19:18:14",
      "6": "2015-08-18 15:02:08",
      "7": "2016-02-03 15:58:49",
      "8": "2017-09-07 22:41:40"
   },
   "Ingredients": {
      "0": "Vodka: 5 cl , Lime: 1/2 , Angostura bitters: 4 dashes , Tonic water: 1 dl Schweppes , Ice: 4 ",
      "1": "Vodka: 2 oz , Half-and-half: 2 oz , Limeade: 2 oz ",
      "2": "Sprite: 1 cup, Lime Juice: 1/2 shot, Vodka: 1 1/2 shot",
      "3": "Vodka: 5 cl, Lemon Juice: 7 cl, Lemon Peel: 1 Slice, Ice: cubes",
      "4": "Vodka: 4 cl, Tonic Water: 10 cl, Lemon Peel: 1 Slice",
      "5": "Water: 2 cups , Sugar: 2 cups white , Coffee: 1/2 cup instant , Vanilla: 1/2, Vodka: 1 1/2 cup",
      "6": "Vodka: 1 1/2 oz , Dry Vermouth: 3/4 oz , Olive: 1 ",
      "7": "Vodka: 2 oz ",
      "8": "Vodka: 2 oz "
   }
}
```
## **Step 3:**
Ending the application:    
```
docker container stop python-container1
```  
Deleting the container:  
```
docker container rm python-container1
```
Deleting the image:  
```
docker image rm cocktail-python
