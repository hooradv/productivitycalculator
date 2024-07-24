import streamlit as st

st.set_page_config(page_title="my webpage", page_icon=":tada:", layout="wide")

st.subheader("hi. Iam a calculator :wave:")
st.title("productivity calculator")


print("Hello, this is a productivity calculator!")
print("put in the numbers and find out how productive you've been.")
print("but remember, this is only a productivity calculator and productivity calculators don't measure importance!\n")
print("Now pick a number from one to ten based on the questions:\n\n")
value = input("value/input(1-10): ")
while float(value) > 10:
    print("that's too much!")
    value = input("value/input(1-10): ")
while float(value) < 1:
    print("that's not enough!")
    value = input("value/input(1-10): ")


frequency = input("frequency(1-10): ")
while float(frequency) > 10:
    print("that's too much!")
    frequency = input("frequency(1-10): ")
while float(frequency) < 1:
    print("that's not enough!")
    frequency = input("frequency(1-10): ")


time_investment = input("time_investment(1-10): ")
while float(time_investment) > 10:
    print("that's too much!")
    time_investment = input("time_investment(1-10): ")
while float(time_investment) < 1:
    print("that's not enough!")
    time_investment = input("time_investment(1-10): ")


health_benefits = input("health_benefits(1-10): ")
while float(health_benefits) > 10:
    print("that's too much!")
    health_benefits = input("health_benefits(1-10): ")
while float(health_benefits) < 1:
    print("that's not enough!")
    health_benefits = input("health_benefits(1-10): ")


skill_development = input("skill_development(1-10): ")
while float(skill_development) > 10:
    print("that's too much!")
    skill_development = input("skill_development(1-10): ")
while float(skill_development) < 1:
    print("that's not enough!")
    skill_development = input("skill_development(1-10): ")


social_impact = input("social_impact(1-10): ")
while float(social_impact) > 10:
    print("that's too much!")
    social_impact = input("social_impact(1-10): ")
while float(social_impact) < 1:
    print("that's not enough!")
    social_impact = input("social_impact(1-10): ")

value = float(value) * 0.4
frequency = float(frequency) * 0.2
time_investment = float(time_investment) * 0.1
health_benefits = float(health_benefits) * 0.15
skill_development = float(skill_development) * 0.1
social_impact = float(social_impact) * 0.05


result = float(value) + float(frequency) + float(time_investment) + float(health_benefits) + float(skill_development) + float(social_impact)

print("here's your productivity result!")
print(result)
