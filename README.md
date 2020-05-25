# ProjectX1(Scrapper)

## Introduction
The intention of this scrapper unlike many is to have a scrapping engine for scrapping websites into different usable structures of data.

### The need
Am on journey to become a data scientist/machine learning engineer and need data to play with and I had the problem of finding a place to rent in the past so I thought could data exploration and machine learning given lots of data and my preferences be able to help me after I spent much money and time looking for houses. This tool is to help me scrape multiple websites for housing data on there. The idea is write once configure multiple times for different websites. 

## Notable requirements:
* This tool should work with multiple websites on demand, to achieve this it is thought that the tool would have an engine that receives a metadata specifying where on the fetched HTML to get required data from.

* This tool shall generate a JSON file with fields and values specified in the metadata as output.


### Assumptions
* It is assumed that the data we would like to scrape would follow a certain structure say for example a paged data listing on a website or a continous feed of data like that on popular webapps like Twitter and Facebook. We have identified some of this popular structures of displaying data on the web and come up with specifications which the end user would use to tell the tool what and where to get the data in a given HTML file.


Sample:\
Scraping https://www.xyzwebsite.ng for all properties on there and having it in a well structured JSON file or scraping a news feed webapp like twitter/facebook this would each require different formats of specifying what to scrape and how to scrape.

## Configuration specifications

Identified data structures diplays
* Paged data list
* News feed like data

### Paged data configuration specification
```json 
{
    "url": "https://www.xyzwebsite.ng",
    "page_query_attr": {
        "query_param_name": "page",
        "start_page": 0,
        "end_page": 1235
    },
    "data_html_attr": {
        "element_name": "div",
        "row_html_attr": "row-data",
        "fields": [
            {
                "element_name": "div",
                "name": "price",
                "class_name": "price"
            },
            {
                "element_name": "div",
                "name": "title",
                "class_name": "title"
            },
            {
                "element_name": "div",
                "name": "description",
                "class_name": "description"
            }
        ]
    }
}
```

## Proposed commands

### Run scrapper on website with metadata
```shell
$ projectx1 -m xyzwebsite.json -o xyzwebsite.csv
```

### View usage and help
```shell
$ projectx1 --help
```

### View version
```shell
$ projectx1 --version
v0.0.1
```