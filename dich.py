from googletrans import Translator
import googletrans
from termcolor import colored

print((colored(r"""
HHHHHHHHH     HHHHHHHHHDDDDDDDDDDDDD        1111111     1111111TTTTTTTTTTTTTTTTTTTTTTT
H:::::::H     H:::::::HD::::::::::::DDD    1::::::1    1::::::1T:::::::::::::::::::::T
H:::::::H     H:::::::HD:::::::::::::::DD 1:::::::1   1:::::::1T:::::::::::::::::::::T
HH::::::H     H::::::HHDDD:::::DDDDD:::::D111:::::1   111:::::1T:::::TT:::::::TT:::::T
  H:::::H     H:::::H    D:::::D    D:::::D  1::::1      1::::1TTTTTT  T:::::T  TTTTTT
  H:::::H     H:::::H    D:::::D     D:::::D 1::::1      1::::1        T:::::T        
  H::::::HHHHH::::::H    D:::::D     D:::::D 1::::1      1::::1        T:::::T        
  H:::::::::::::::::H    D:::::D     D:::::D 1::::l      1::::l        T:::::T        
  H:::::::::::::::::H    D:::::D     D:::::D 1::::l      1::::l        T:::::T        
  H::::::HHHHH::::::H    D:::::D     D:::::D 1::::l      1::::l        T:::::T        
  H:::::H     H:::::H    D:::::D     D:::::D 1::::l      1::::l        T:::::T        
  H:::::H     H:::::H    D:::::D    D:::::D  1::::l      1::::l        T:::::T        
HH::::::H     H::::::HHDDD:::::DDDDD:::::D111::::::111111::::::111   TT:::::::TT      
H:::::::H     H:::::::HD:::::::::::::::DD 1::::::::::11::::::::::1   T:::::::::T      
H:::::::H     H:::::::HD::::::::::::DDD   1::::::::::11::::::::::1   T:::::::::T      
HHHHHHHHH     HHHHHHHHHDDDDDDDDDDDDD      111111111111111111111111   TTTTTTTTTTT  
║[*]Created by Hd11T[*]║""",'green')))    

#Dịch Ngôn Ngữ Việt Anh Bởi Hà Duy Thành
print((colored("\n[*]Lưu Ý Cách Sử dụng[*]", 'yellow')))
print("『Nếu Nhập Chữ Cần Dịch Là Tiếng Việt Thì Ngôn Ngữ Nhập en』")
print("『Nếu Nhập Chữ Cần Dịch Là Tiếng Anh Thì Ngôn Ngữ Nhập vi』\n")
text=en=input("[Nhập chữ cần dịch]:")
text=vi=input("[Nhập ngôn ngữ muốn dịch]:")
if text ==en:
    print(lang=en)
else: 
    text ==vi
translated = Translator().translate(en, dest=vi).text

if text ==en:
    print("Tiếng Việt:")
else:
    print((colored("\n[Bản Được Dịch Ra]:", 'red')))
print(translated)

