import streamlit as st
st.title("Hello")
st.header("This is header")
st.subheader("This is subheader")
st.text("This is our project")
st.markdown("### This is a markdown")
#Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing the widge")

# Radion Button
# Create a Radion button to select gender
status = st.radio("Select Gender:", ["Male", "Female"])

#Display the selected option using success  message
if status == "Male":
    st.success("Male")
else:
    st.success("Female")

#Selection box
# Create a Radion button to select gender
Hobby = st.selectbox("Select your hobby:", ["Dancing", "Reading", "Sleeping"])

#Display the selected hobby
st.write("Your hobby is: ", Hobby)

#Multi-Select Box
# create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select your hobbies: ", ['Dancing', "Reading", "Sleeping"])

# Display the number of selected hobbies
st.write("You Selected", len(hobbies), "hobbies")

# Button
st.button("Click")

if st.button("About"):
    st.text("Welcome to streamlit")

# Text Input
name = st.text_input("Entr you name: ")

if st.button("Submit"):
    result = name.title()
    st.success(result)

#Slider 
level = st.slider("Choose a level", min_value=1, max_value=5)

st.write(f"Selected level : {level}")