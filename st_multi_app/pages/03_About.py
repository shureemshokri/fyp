import streamlit as st

def main():
    st.title("About")
    st.subheader("Glad you are excited to know more about this application!")
    st.text("This project is a collaboration between FSKTM and a lecturer in")
    st.text("Universiti Putra Malaysia, Dr Sarah, who is a lecturer in Fakulti Pertanian.")
    st.subheader("Please leave a comment or input for this project. It will help us a lot to improve this project!")
    st.text_input("Please input data here.")

if __name__ == "__main__":
    main()