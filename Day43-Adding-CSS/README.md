Day 43

Introduction to CSS - Cascading Style Sheets


# Inline CSS (for 1 element)

<html style="background:blue">
</html>

# Internal CSS (for 1 webpage)

Usually put in `head` segment

<head>
    <style>
        h1{
            color: red;
        }
    </style>
<head>

# External CSS - It has a self-closing tag and a link to point to another css file (for 1 or more websites)


<head>
    <link
        rel="stylesheet" 
        type="text/css"
        href="./styles.css"
    />
</head>


Element Selector - targets the h1 tag
h1{
    color:blue;
}
Class Selector - targets the class tags - many elements
<h2 class="red-text">Red</h2>
.red-text{
    color: red
}

Universal selector - apply to all elements in page
*{
    color:red;
}

Id Selector - one element - completely unique
<h2 id="main">Red</h2>

#main{
    color:red
}

Attribute selector
<a href= attribute=></a>
a[atrribute] {
    color: red;
}

![Alt text](image.png)
![Alt text](image-1.png)
![Alt text](image-2.png)
![Alt text](image-3.png)
![Alt text](image-4.png)
![Alt text](image-5.png)