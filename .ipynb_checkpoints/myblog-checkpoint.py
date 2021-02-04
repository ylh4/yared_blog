#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:54:53 2021

@author: yaredhurisa
"""
import streamlit as st
import psycopg2

connection = psycopg2.connect(
    host='blog-db-instance.ci8xktvcnk4v.us-west-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='Enateye051',
    database='blog_db'
)
cursor = connection.cursor()
