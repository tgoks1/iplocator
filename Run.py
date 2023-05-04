import requests;
import json;
def iplookup(ip_address):
    data_return = requests.get("http://ipapi.co/" + ip_address + "/json/",{});
    return json.loads(data_return.content);
print("""\033[1;32m\n     
   /  _/___  / /   ____  _________ _/ /_____  _____
   / // __ \/ /   / __ \/ ___/ __ `/ __/ __ \/ ___/
 _/ // /_/ / /___/ /_/ / /__/ /_/ / /_/ /_/ / /    
/___/ .___/_____/\____/\___/\__,_/\__/\____/_/     
   /_/                           by.The-Goks                                            
                              
Version : 1.0
Github :\033[1;36m https//github.com/tgoks1
""");
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
def mulai(ip_addressnya):
    result_track = iplookup(str(ip_addressnya));
   
    if "error" in result_track:
        if result_track['reason'] == "RateLimited":
            print(f"{RED}Failed to check! Too many request! retrying...");
            mulai(ip_addressnya);
        else:
            print(f"{RED}{result_track['reason']}");
        
    else:
        print(f"""{BLUE}IP ADDRESS : {LIGHT_CYAN}{result_track['ip']}
{BLUE}ASN : {LIGHT_GREEN}{result_track['asn']}
{BLUE}ORG : {LIGHT_GREEN}{result_track['org']}
{BLUE}NETWORK : {LIGHT_GREEN}{result_track['network']}
{BLUE}VERSION : {LIGHT_GREEN}{result_track['version']}
{BLUE}CITY : {LIGHT_GREEN}{result_track['city']}
{BLUE}REGION : {LIGHT_GREEN}{result_track['region']}
{BLUE}REGION CODE : {LIGHT_GREEN}{result_track['region_code']}
{BLUE}COUNTRY : {LIGHT_GREEN}{result_track['country']}
{BLUE}COUNTRY NAME : {LIGHT_GREEN}{result_track['country_name']}
{BLUE}Country Code ISO : {LIGHT_GREEN}{result_track['country_code_iso3']}
{BLUE}Country Capital : {LIGHT_GREEN}{result_track['country_capital']}
{BLUE}Country Tld : {LIGHT_GREEN}{result_track['country_tld']}
{BLUE}Continent code : {LIGHT_GREEN}{result_track['continent_code']}
{BLUE}Postal Code : {LIGHT_GREEN}{result_track['postal']}
{BLUE}Latitude : {LIGHT_GREEN}{result_track['latitude']}
{BLUE}Longitude : {LIGHT_GREEN}{result_track['longitude']}
{BLUE}Timezone : {LIGHT_GREEN}{result_track['timezone']}
{BLUE}UTC : {LIGHT_GREEN}{result_track['utc_offset']}
{BLUE}Calling code : {LIGHT_GREEN}{result_track['country_calling_code']}
{BLUE}Currency : {LIGHT_GREEN}{result_track['currency']}
{BLUE}Currency Name : {LIGHT_GREEN}{result_track['currency_name']}
{BLUE}Languages : {LIGHT_GREEN}{result_track['languages']}
{BLUE}Country Area : {LIGHT_GREEN}{result_track['country_area']}
{PURPLE}Country Population : {LIGHT_GREEN}{result_track['country_population']}
""");
    start();
def start():
    print(LIGHT_GREEN);
    ip_addressnya = input("IP ADDRESS : ")
    mulai(ip_addressnya);
    
start();