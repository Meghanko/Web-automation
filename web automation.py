import webbrowser as wb

def webautomation():
    chrome_path = '"path/chrome.exe" %s'
    URLS = (
        	"stackoverflow.com", 
	        "flipkart.com",
            "codeforces.com",
	        "indiatoday.com",
	        "economictimes.com"
    )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)

webautomation()