text = "X-DSPAM-Confidence:    0.8475";
text1 = text.find("0")
text = text[23:]
Text = float(text)
print(Text)