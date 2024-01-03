#Console UI.py, Will be what gives Manager.py what needs to be changed
import logging
from datetime import date
import os
import Save
import logs

logs.info("Console UI.py Started Successfully!")


rule = input("Enter a rule / action \nsee Docs.md for help\n-")


splitrule = f"{rule.split(' ')[0]} {rule.split(' ')[1]}"

splitaction = f"{rule.split(' ')[2]} {rule.split(' ')[3]}"

print(f"Rule: {splitrule}")

print(f"Action: {splitaction}")

logs.info("Saving Rules / Actions...")
Save.Save({
    "Rule" : splitrule,
    "Action" : splitaction
})