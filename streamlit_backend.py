#import streamlit as st


# st.title("Our first streamlit Application")
# st.write("Welcome to Gen AI World!!!!!!!!!!!!!!")


#Text
#Elements


#st.title("This is the title function")
#st.header("This is a header")
#st.subheader("This is a subheader")
#st.text("This is the text")
#st.write("write can display anything")
#st.markdown("**Bold text** and *italic text*")



#input widgets


# name = st.text_input("What is ur name?")
# st.write(f"Hello (name)")
# st.write("(without f string) Hello (name)")





#age = st.number_input("how old are you", min_value=1, max_value=105)
#st.write(f"you are {age} years old!")



#slider


#temperature = st.slider("select temperature", 0,100,25)
#st.write(f"temperatyure is (temperature)")





 #Button

 
 #if st.button("Click Me"):
 # st.write("Button was clicked")
 # st.balloons()





#select box

# option = st.selectbox(
#          "choose your fvaourite fruit",
#          ["apple", "banana", "orange"]
# )
# st.write(f"you selected {option}")




#layout components


# col1, col2 = st.columns(2)

# with col1:
# st.header("Left side")
#   st.write("This is on the left")



#with co12:

#st.header("right side")
# st.write("This is right side")



#side bar

# st.sidebar.title("Settings")
# option = st.sidebar.selectbox("choose", ["Account setting","AI Copilot"])



#st.sidebar.title("Settings")
#option = st.sidebar.selectbox("choose", ["Account setting", "AI copilot"]


#st.sidebar.radio()



#Browse button

# uploaded_file = st.file_uploader("Choose a file", key="file_uploader")

# if uploaded_file is not Done:

# st.write(f"File {uploaded_file.name} uploaded successfully!")