![Logo of this Script](https://raw.githubusercontent.com/4rr0w/Golden-Darknesss/master/Golden-Darknesss.png)


# Golden-Darknesss
My first python script which finds list of meaningful words based on some constrained given by user and it also stores those words in a text file. So basically it can be used to create a word-list.>
It scraps the https://morewords.com to find all those words. use this script on your risks and i don't recommend using this for any wrong purpose. I just made this for exploring that website and beautiful soup library as a beginner.

#Usage:
clone this repo. and run
-> pip3 install -r requirements.txt
for usage instructions lets take an example::


->python3 golden-darknesss.py -l  9  -s  a  -e  e  -i  4  -b  s 

This will return words which contains 9 letters, first letter is 'a' (usage of -s), ending with letter 'e' (usage of -e),
and contain s at their 4th index (usage of -i and -b)(remember index starts from 0)  for example 'aerospace' will be one of those words which this script will print( and  save in a text file in same directory) when you run the this script with above inputs.

It also provides a custom search if user wants also if length is unknown you can mention it by using '-u' then it will find all possible words for all lengths. 
further you can explore.

in further versions the time it takes to find words can be reduced which i feel is really high.

a big thanks to somdev sangwan(s0md3v) <3
