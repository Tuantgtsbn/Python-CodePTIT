# import re

# # Đọc văn bản từ input
# text = ""
# while True:
#     try:
#         line = input()
#         text += line + " "  # Thêm một khoảng trống để duyệt qua các dòng liên tiếp
#     except EOFError:
#         break

# # Tìm và thay thế các câu theo yêu cầu
# sentences = re.findall(r'[^.!?]+[.!?]*', text)

# for sentence in sentences:
#     # Loại bỏ khoảng trống ở đầu và cuối câu
#     sentence = sentence.strip()
    
#     # Ký tự đầu viết hoa, các ký tự còn lại viết thường
#     sentence = sentence[0].upper() + sentence[1:].lower()
    
#     # Điền thêm dấu chấm nếu cần
#     if not sentence.endswith('.') and not sentence.endswith('!') and not sentence.endswith('?'):
#         sentence += '.'

#     print(sentence)
delim = '.!?'

a = []

while True:
    try:
        s = input()
        s = s.lower()
        s = s.strip()
        x = ''
        for i in s:
            if i in delim:
                x = x.strip()
                if len(x) > 0:
                    x += i
                    a.append(x)
                x = ''
            else:
                x += i
        x = x.strip()
        if len(x) > 0:
            a.append(x)
    except Exception:
        break

for i in a:
    s = i.split()
    res = ''
    for j in s:
        if len(j) > 0:
            res += j + ' '
    res = res[:len(res) - 1]
    if res[-1] not in delim:
        res += '.'
    res = res.capitalize()
    print(res)