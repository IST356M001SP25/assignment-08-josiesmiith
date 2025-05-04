# Reflection

Student Name:  Josie Smith
Sudent Email:  jsmit194@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

In this assignment I used streamlit, matplot, seaborn, geopandas, and pandas to wrangle some data and store different aggregations of it into different csv files in the cache, then display that data in an interactive dashboard with a map, a dropdown menu, and two bar charts. Once again, the real struggle was in getting my tests to show up in the first place. I spent about an hour checking pathways and checking pytest because "code" wasn't being recognized as a package and I kept on getting "ModuleNotFound" errors for the code folder. It took a long time and I relyed pretty heavily on ChatGPT, showing it my error messages and my outputs. Through that struggle I learned how important folder structure is and how everything must be in the right order and the pathway directory must be correct for anything to work. I used previous debugging knowledge to verify that pytest was being used for testing, not unittest.
As for the assignment itself, a lot of the time CoPilot will give me better code if I put markdown above it or write what I want it to do in comments. I don't want to rely on this, but it makes life a lot easier and I make sure to type it out instead of just pressing tab so that I better understand what it's putting in. I worked with the merge function and got more practice writing csv files to a cache. I still don't fully understand the streamlit st.metric() function, or why subplots are necessary/what they do for plotting within the location dashboard. 