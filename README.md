# Web Crawler

Web crawler for webpage  https://news.ycombinator.com/. The present package allow to extract the first 30 entries from the webpage  and extract the following information:

 * Title
 * Number of the order
 * Number of comments
 * Points

Moreover, the package implement functions for filtering and sorting the data obtained.

## Install Requirements
First in order to use the package is recommendable to install the requirements

``` 
pip install -r requirements.txt
```

## Run Code

The code filter the titles with more than 5 words and sort the data in dependence to the requirements of the user. The code show on screen the filtered data an return a file with the filtered and sorted data.  

Run the code:
```
python web_crawler.py <Type of Sorting> <Argument to Sort> <Type of Output File> <Name of Output File>
```
* **Type of Sorting** .- Define if the sort is ascending (asc) or descending (desc)
* **Argument to Sort**.- Specify with argument from the data you want to sort (Number of order, Number of comments, points/score )
* **Type of Output File**.- Define with kind of output file do you requirer (csv, txt, out). The option csv is think for further data processing of the filtered data. The options *txt*, *out* are think for visualization of the user.
* **Name of Output File**.- Specify the name of your output file
  
If you want to display this information in your console you can run:

```
python web_crawler.py -h
```
## Test

To run the test:
```
python test.py
``` 
or 
```
pytest -q test.py
```

## Future Work

It is important to remark that the file *data_manager.py* allow to work with any list of objects that can be filtered and sorted. In this sense, this part of the package can be extended to perform more complicated operations on a list of objects or to perform more complicated filtering to the actual data.

As an example, it is possible to define a different type of filtering by making use of the function:
```
 def filter_news(self,attrib: str, __boolF)-> None:
```
where:
  
  * **attrib**.- makes reference to the attribute from the class news that you can to filter
  * **__boolF**.- refer to some function tha return a bool.
