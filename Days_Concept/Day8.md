# Dictionaries and Nesting
They group together the words and helps to search the word easily exactly the same as real life dictionaries.

It's having two main parts: Key and Value
> {key: value}

More than one key and values:
> dict= {  
    key1:value1,    
    key2:value2,   
    key3: value3,   
    key4:value4  
    }

example: 
> dict={  
    "Hello": "Greeting",  
    "Modest": "humble",  
    "canny": "rude"  
}    

### Should use the correct syntax to define the keys
Accesing the elements of dictionary: We can with the help of a key
> print(dic["key1"])  
> print(dic["key2"])  

> dict= {  
    1: "One",  
    2: "Two",    
    3: "Three"  
}

> print(dict[1])

## Adding more keys and value in the dictionary:
> dic["intution"]= "Give brief introduction to something"  
print(dic)

Output: Dicctionary with newly added key

## Create an empty dictionary

>sample_dictionary = {}

>dic ={}  
output: Make our existing dictionary empty

## Edit an existing dictionary
> dic["canny"]= "Bad Behaviour"

Note: It will find the key in the dictionary and if it is found in it then edit it with a new value, if not then append at the end

## Loop through a dictionary

> for key in dict:  
    print(key)  
    print(dict[key])

Output: 
* Print all the keys  
* Print all the values  

## Nesting Lists and Dictionaries

Nesting:  
### List inside the dictionary as value

> dict = {  
    "key1": ["value1", "value2"..],  
    "key2": "anything"  
}

### Dictionary inside the dictionary

> dict = {  
    "key1": {"sub_key1": ["value1", "value2"]},  
    "key2": "anything"  
}

### Dictionary in list

> dict =[  
    {"key1": ["value1", "value2", "value3"],   "key2": ["anything1", "anything2"] },  
    {"key3": ["value4", "value5"],  
    "key4": "Anything"}
]

## Quiz Questions:

1. ![image](/Days_Concept/photos/Quiz1.png)
2. ![image](/Days_Concept/photos/Quiz2.png)
3. ![image](/Days_Concept/photos/Quiz3.png)

Note: 
> from replit import clear  
clear() *clears the screen*