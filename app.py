import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

# Define your Hugging Face account email and password
email = "hamzamurtaza11@gmail.com"
passwd = "Dz8@1=%Kb07Xs"

# Log in to Hugging Face and grant authorization to HuggingChat
sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

# Load cookies when you restart your program:
# sign = Login(email, None)
# cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


# Streamlit UI

st.markdown(
    """
    <script>
        window.scrollTo(0, 0);
    </script>
    """,
    unsafe_allow_html=True
)
# Assuming your image file is in the same directory as your script
image_path = "bawdicsoft_logo.jpg"

# Set the width of the image (in pixels or as a percentage of column width)
#image_width_pixels = 300
image_width_percentage = 70

# Add an image to your Streamlit app with specified width
#st.image(image_path, caption="", width=image_width_pixels)

st.image(image_path, caption="", width=image_width_percentage)


st.title("BofT")
st.subheader("Hello, ask me anything...")
#st.sidebar.title("Settings")
st.markdown('<style>h1 { color: #000080; }</style>', unsafe_allow_html=True)
#st.markdown('<p style="color:#000080 ;">This is a paragraph with custom font color.</p>', unsafe_allow_html=True)

# Function to query the chatbot and display responses
def query_and_display(query, stream=False):
    if stream:
        for resp in chatbot.query(query, stream=True):
            st.text(resp)
    else:
        response = chatbot.query(query)
        st.text(response)










# Apply the styles to the input box

#st.markdown('<p style="color:#000080 ;">Enter your message</p>', unsafe_allow_html=True)
query_input = st.text_input("Enter your message")
stream_checkbox = 0
st.markdown("<br><br>",unsafe_allow_html=True)
if st.button("Send"):
    #st.text("User: " + query_input)
    if stream_checkbox:
        query_and_display(query_input, stream=True)
    else:
        query_and_display(query_input)

# Web Search UI
# web_search_checkbox = st.checkbox("Enable Web Search")

# if web_search_checkbox:
#     web_search_query = st.text_input("Web Search Query:")
#     if st.button("Search"):
#         query_result = chatbot.query(web_search_query, web_search=True)
#         st.text("Web Search Results:")
#         for source in query_result.web_search_sources:
#             st.text(f"{source.title} - {source.link}")

# # Conversation Information UI
# conversation_info = chatbot.get_conversation_info()
# st.sidebar.header("Conversation Information")
# st.sidebar.text(f"Conversation ID: {conversation_info.id}")
# st.sidebar.text(f"Conversation Title: {conversation_info.title}")
# st.sidebar.text(f"Current Model: {conversation_info.model}")
# st.sidebar.text(f"System Prompt: {conversation_info.system_prompt}")
# st.sidebar.text(f"Conversation History: {conversation_info.history}")

# Additional Options
# st.sidebar.header("Additional Options")
# if st.button("Get Conversation List"):
#     conversation_list = chatbot.get_conversation_list()
#     st.text("Conversation List:")
#     for conv in conversation_list:
#         st.text(f"{conv['id']} - {conv['title']}")

# if st.button("Get Available Models"):
#     available_models = chatbot.get_available_llm_models()
#     st.text("Available Models:")
#     for i, model in enumerate(available_models):
#         st.text(f"{i + 1}. {model}")

# Delete All Conversations (DANGER)
# if st.button("Delete All Conversations"):
#     confirmation = st.checkbox("I understand that this action is irreversible.")
#     if confirmation and st.button("Confirm Deletion"):
#         chatbot.delete_all_conversations()
#         st.text("All conversations have been deleted!")

# # Run the Streamlit app
# if __name__ == "__main__":
#     main()
  

