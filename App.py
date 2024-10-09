import streamlit as st

# Define the lessons data
lessons = [
    {"title": "Starting the Day", 
     "description": "A well-prepared start can set the tone for the entire workday. "
                    "In this lesson, we discuss the importance of being mentally and physically prepared, "
                    "understanding your tasks, and ensuring you are equipped to handle customer needs effectively."},
    
    {"title": "Listening Skills", 
     "description": "Active listening is a cornerstone of excellent customer service. "
                    "Learn techniques to actively engage with customers, understand their concerns, "
                    "and respond in a way that shows empathy and understanding."},
    
    {"title": "Attention to Detail", 
     "description": "The small details can make a big difference in the customer experience. "
                    "This lesson focuses on how attention to detail, from a customer's name to their preferences, "
                    "can enhance their satisfaction and ensure repeat business."},
    
    {"title": "Multitasking", 
     "description": "In a fast-paced environment, multitasking becomes essential. "
                    "This lesson covers strategies for managing multiple customer interactions or tasks simultaneously, "
                    "without sacrificing quality or care."},
    
    {"title": "Friendly Attitude", 
     "description": "A positive and approachable demeanor is essential in customer service. "
                    "In this lesson, we emphasize the importance of maintaining a friendly attitude even in stressful situations, "
                    "as this can defuse tension and leave a lasting positive impression."},
    
    {"title": "Team Player", 
     "description": "Customer service is often a team effort. "
                    "Learn how to collaborate with your colleagues to deliver seamless service and ensure every customer leaves satisfied."},
    
    {"title": "Customer Connection", 
     "description": "Building a connection with customers goes beyond addressing their immediate needs. "
                    "This lesson teaches you how to foster long-term relationships through personal engagement and genuine interest."},
    
    {"title": "Communication", 
     "description": "Clear and concise communication is key to avoiding misunderstandings. "
                    "In this lesson, we explore how to deliver important information in a way that is both effective and respectful."},
    
    {"title": "Empathy", 
     "description": "Understanding a customer's emotional state is crucial. "
                    "This lesson teaches you how to put yourself in the customer's shoes and respond in a way that validates their concerns."},
    
    {"title": "Problem-solving", 
     "description": "Customers don’t want to hear excuses, they want solutions. "
                    "Learn how to resolve issues efficiently, whether it's a product defect or a service failure, "
                    "and turn potentially negative experiences into positive outcomes."}
]

# Define the themes data
themes = [
    "Introduction and Background",
    "Entrepreneurial Ventures",
    "Work Experience",
    "Customer Service Skills",
    "Training Course Details",
    "Benefits for Businesses",
    "Importance of Great Service"
]

# Define Home Benefits content
home_benefits = {
    "individuals": [
        "Enhance your communication and interpersonal skills",
        "Become more efficient at multitasking and managing stress",
        "Develop empathy and active listening techniques",
        "Improve problem-solving abilities in high-pressure situations",
        "Build customer relationships and drive repeat business"
    ],
    "businesses": [
        "Increase customer satisfaction and retention rates",
        "Develop a customer-focused company culture",
        "Improve team collaboration and service consistency",
        "Boost brand reputation through excellent customer service",
        "Drive revenue growth through loyal customer advocacy"
    ]
}

# Define function for each lesson page
def lesson_page(lesson):
    st.title(f"Lesson: {lesson['title']}")
    st.write(lesson['description'])

# Define function for themes page
def themes_page():
    st.title("Key Themes Discussed")
    for theme in themes:
        st.write(f"- {theme}")

# Define function for blog post page
def blog_page():
    st.title("The Power of Excellent Customer Service: Lessons from Erica Penson")
    st.subheader("Unveiling the Secrets Behind Developing an Enduring Customer Experience")
    st.write("""
    Customer service is the lifeline of any thriving business. It can make or break the brand loyalty that businesses strive to build. 
    In a recent event, Erica Penson shared her knowledge on delivering exceptional customer service. Let's dive into the key points.
    
    ### Introduction to Erica Penson and Her Ventures
    Erica Penson is a seasoned entrepreneur, the owner of multiple brands including Forever Lit Hookah, Everlit Hookah, and Everlit Essentials.
    
    ### The Essence of Great Customer Service
    Great customer service goes beyond transactions. It's about creating memorable experiences that encourage customers to return.
    
    ### Benefits of Excellent Training
    Erica emphasizes that comprehensive training is a key investment for businesses aiming to deliver outstanding service.
    
    ### Practical Takeaways for Business Owners
    - Invest in Training
    - Encourage Empathy
    - Focus on Consistency
    - Solicit Feedback
    
    In conclusion, the power of excellent customer service transforms businesses into beloved brands.
    """)

# Define function for home benefits page
def home_benefits_page():
    st.title("Benefits of Completing E Clanton's Customer Service Training")

    st.subheader("For Individuals:")
    for benefit in home_benefits["individuals"]:
        st.write(f"- {benefit}")

    st.subheader("For Businesses:")
    for benefit in home_benefits["businesses"]:
        st.write(f"- {benefit}")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "Lessons", "Themes", "Blog Post", "Home Benefits"])

# Home Page
if page == "Home":
    st.title("Welcome to E Clanton Customer Service Training")
    st.write("""
    This comprehensive customer service training program, led by Erica Penson, will guide you through essential skills that are crucial in delivering exceptional service. 
    With a focus on real-world applications, you will gain insights into how to interact with customers, solve problems, and foster lasting connections.
    
    Use the navigation sidebar to explore the training lessons, key themes, and a blog post summarizing Erica's powerful approach to customer service. Additionally, learn about the benefits of completing this course, both for you and your business.
    """)

# Lessons Page
elif page == "Lessons":
    lesson_choice = st.sidebar.selectbox("Select a lesson", [lesson['title'] for lesson in lessons])
    lesson = next(lesson for lesson in lessons if lesson['title'] == lesson_choice)
    lesson_page(lesson)

# Themes Page
elif page == "Themes":
    themes_page()

# Blog Post Page
elif page == "Blog Post":
    blog_page()

# Home Benefits Page
elif page == "Home Benefits":
    home_benefits_page()
