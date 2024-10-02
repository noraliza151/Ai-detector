def check_watermark(text):
    watermark_pattern = [' ', '  ', '  ', ' ']
    words = text.split(' ')
    observed_pattern = []
    for i in range(len(words) - 1):
         space_length = len(text.split(words[i])[1]) - len(words[i+1])
         observed_pattern.append(' ' * space_length)
    return observed_pattern == watermark_pattern[:len(observed_pattern)]
watermarked_text = input("put the text that you want to test")
non_watermarked_text = "This is not watermarked"
print("Watermarked Text Check:", check_watermark(watermarked_text))
print("Non-Watermarked Text Check:", check_watermark(non_watermarked_text))