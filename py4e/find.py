text = "X-DSPAM-Confidence:    0.8475";
text2 = text.find('0.8475')
print(float(text[text2:]))
