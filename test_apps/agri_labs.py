"""
title: Agri lab problems resolver
description: This program facilities entry of laboratory observations into a CSV file
author: D.D. Saushkin
requirements:
    functionality:
        Allow all relevant, valid data to be entered, as per the data dictionary.
        Append all valid data to CSV file: CSV file must have a filename of abq_record_CURRENTDATE.csv,
        where CURRENTDATE is the date of the laboratory observations in ISO format (YYYY-MM-DD).
        The CSV must include all fields listed in the data dictionary.
        The CSV headers will avoid cryptic abbreviations. Enforce correct datatypes per field.
    non-functionality:
        Enforce reasonable limits on data entered, per the data dict.
        Autofill data to save time.
        Suggest likely correct values.
        Provide a smooth and efficient workflow.
        Store data in format easily understandable by Python.
functionality not required:
    Allow editing of data.
    Allow deletion of data.
limitations:
    Program must be efficiently operable by keyboard-only users.
    Be accessible to colorblind users.
    Run acceptably on low-end PC.
"""

import tkinter as tk


