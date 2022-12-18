# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_test_albert.py
@Time: 2022-10-27 15:25
@Last_update: 2022-10-27 15:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from transformers import AutoModelForSequenceClassification


model = AutoModelForSequenceClassification.from_pretrained("bert-large-uncased").to("cuda")
print('here')
print('here')