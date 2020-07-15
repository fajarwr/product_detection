# Product Detection

Product detection simple web apps based on Shopee Code League Competition.  
[Shopee code league](https://careers.shopee.sg/codeleague/)  
[Kaggle product detection](https://www.kaggle.com/c/shopee-product-detection-open)

## Train the model

* Open : Competition_2_Product_Detection_Submitted.ipynb.  
* Train the model in your google colab.
* Feel free to train your own CNN architecture.
* Download the latest model weight.

## Install django

* Install django [here](https://docs.djangoproject.com/en/3.0/topics/install/)  
* Go to directory : ```cd product_detection```  
* Make weight folder : ```mkdir weights```  
* Place the trained weight model into a weights folder  
  ```
  product_detection/
    category_detail/
      detail.csv
    product_detection/
      __init__.py
      asgi.py
      settings.py
      urls.py
      views.py
      wsgi.py
    templates/
      index.html
    weights/
      your-weights.hdf5
    Competition_2_Product_Detection_Submitted.ipynb
    manage.py
  ```
* Run the django  
  ```python
  python manage.py runserver
  ```  

## Usage
* Open localhost:8000
* Predict some sample product image [here](https://drive.google.com/file/d/1bPZilovvLBj8_4b6RaAYqES2N-MCeRqJ/view?usp=sharing)
* Get the result  
![alt text](https://github.com/fajarwr/product_detection/product_detection.gif)

## Support
Reach me out & feel free to discuss!  
* Linkedin at  [linkedin.com/in/fajar-wr/](https://www.linkedin.com/in/fajar-wr/)  
* Github at [github.com/fajarwr](https://github.com/fajarwr)  
