print("=====customer record cleaner=========")
raw_name = " rahul VERMA "
raw_email = " Rahul.Verma@NimbusMail.COM "
raw_company = "nimbus software pvt ltd"
signup_code = "CUST-2026-00873"
raw_name1= ((raw_name.strip()).title())#name(strip + title case)
print(raw_name1)
raw_email2=((raw_email.strip()).lower())#email(strip + lowercase).
print(raw_email2)
print(raw_email2[12:])# email domain(everything after @ )
print(raw_email2.find("@"))#find("@")
print(int(signup_code[-4:]))#the last 5characters and print it without leading zeros (convertwithint()
print(raw_company.title())#display_company : title-case
print(raw_email2.endswith("com"))
print(raw_company.startswith("nimbus"))
print("="*30)
