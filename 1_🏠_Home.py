import streamlit as st
import openai
import utils

# OpenAI setup
openai.api_key = utils.open_file('openai_api_key.txt')

# Set page config
utils.set_page_configuration(initial_sidebar_state="collapsed")
utils.set_sidebar()

# Intro
title = 'Smart Sales Assistant'
subtitle = "Boost Your Sales Success with AI-Powered Support"
mission = "Supercharge your sales efforts with the cutting-edge AI-powered sales assistant. Identify high-quality prospects, craft compelling cold emails, and gather valuable company information effortlessly to maximize your productivity and close deals faster!🚀"
utils.display_intro(title=title, subtitle=subtitle, mission=mission)

# Content
st.text('')
st.image('static/home_banner.png')

name_1 = f"🎯 Find next best company"
desc_1 = f"Never waste time on unqualified leads again. Our AI assistant uses advanced algorithms to analyze vast amounts of data and identify the most promising prospects for your business. Discover hidden opportunities, reach out to decision-makers, and watch your pipeline grow with high-quality leads."
page_1 = "Find_Next_Best_Company"
name_2 = f"🔎 Scrape Company Information"
desc_2 = f"Accessing valuable company information has never been easier. Our AI assistant can swiftly gather relevant data about any company from various sources across the internet. From financials and industry trends to key stakeholders and recent news, you'll have the insights you need to establish meaningful connections and build rapport"
page_2 = "Scrape_Company_Information"
name_3 = f"🔮 Predict Company Intent"
desc_3 = f"Qualify your leads thanks to this AI that classifies the intent of a B2B website page (high, medium, low, none) based on its content"
page_3 = "Predict_Company_Intent"
name_4 = f"📝 Craft Personalized Cold Emails"
desc_4 = f"Say goodbye to generic and ineffective cold emails. Our smart sales assistant generates highly personalized and engaging email templates tailored to each prospect. With AI-driven insights, it helps you understand your target audience better and ensures your messages resonate with them, increasing your chances of a positive response."
page_4 = "Craft_Personalized_Cold_Emails"

tools = [
    {'name':name_1, 'desc': desc_1, 'page': page_1},
    {'name':name_2, 'desc': desc_2, 'page': page_2},
    {'name':name_3, 'desc': desc_3, 'page': page_3},
    {'name':name_4, 'desc': desc_4, 'page': page_4}
]

for tool in tools:
    utils.display_tool(name=tool['name'], desc=tool['desc'], page=tool['page'])