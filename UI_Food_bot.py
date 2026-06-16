import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize Mistral Model
model = init_chat_model(
    model="mistral-small-2506",
    api_key=st.secrets['MISTRAL_API_KEY']
)
    
    "MISTRAL_API_KEY")

# Page Config
st.set_page_config(
    page_title="AI Indian Master Chef",
    page_icon="🍛",
    layout="wide"
)

# System Prompt
SYSTEM_PROMPT = """
You are Chef Bharat, a world-class Indian Master Chef with over 30 years of experience in Indian cuisine.

Your responsibility is to suggest authentic Indian recipes based on the ingredients provided by the user.

Rules:
1. Always suggest at least 2 Indian recipes whenever possible.
2. Use the ingredients provided by the user as much as possible.
3. Assume common kitchen ingredients like salt, oil, water, turmeric, chilli powder, cumin, coriander powder and garam masala are available.
4. For each recipe provide:
   - Recipe Name
   - Ingredients Used
   - Additional Ingredients Required
   - Preparation Time
   - Cooking Time
   - Difficulty Level
   - Step-by-Step Instructions
5. Keep recipes authentic and practical.
6. End with a Chef Recommendation.
"""

# Header
st.markdown(
    """
    <h1 style='text-align:center;'>🍛 AI Indian Master Chef</h1>
    <h4 style='text-align:center;color:gray;'>
    Select ingredients and generate delicious Indian recipes
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

# Ingredients List
ingredients_list = [
    "Onion",
    "Tomato",
    "Potato",
    "Paneer",
    "Rice",
    "Peas",
    "Capsicum",
    "Carrot",
    "Beans",
    "Cabbage",
    "Chicken",
    "Egg",
    "Garlic",
    "Ginger",
    "Green Chilli",
    "Spinach",
    "Corn",
    "Mushroom",
    "Cauliflower",
    "Cheese"
]

selected_ingredients = st.multiselect(
    "🛒 Select Available Ingredients",
    ingredients_list
)

col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button(
        "🍳 Generate Recipes",
        use_container_width=True
    )

with col2:
    clear_btn = st.button(
        "🗑️ Clear",
        use_container_width=True
    )

if clear_btn:
    st.rerun()

if generate_btn:

    if not selected_ingredients:
        st.warning("Please select at least one ingredient.")
        st.stop()

    ingredient_string = ", ".join(selected_ingredients)

    user_prompt = f"""
Available Ingredients:
{ingredient_string}

Suggest at least 2 authentic Indian recipes using these ingredients.
"""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_prompt)
    ]

    with st.spinner("👨‍🍳 Chef Bharat is preparing recipes..."):

        try:
            response = model.invoke(messages)

            st.success("Recipes Generated Successfully!")

            st.markdown("## 📖 Recommended Recipes")
            st.markdown(response.content)

        except Exception as e:
            st.error(f"Error: {e}")
