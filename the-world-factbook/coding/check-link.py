import requests


class checkLink():
    def __init__(self, file_name):
        self.file_name = file_name

    def check(self):
        f = open(self.file_name, "r")

        for i in f:
            i = i.strip("\n")
            print(f'{i} : {requests.get(f"https://www.cia.gov/the-world-factbook/countries/{i}")}')


check_link = checkLink("../field/country-names.txt")
check_link.check()

### Output
# C:\Users\woosal\Anaconda3\python.exe D:/GitHub/CIA/the-world-factbook/coding/check-link.py
# <_io.TextIOWrapper name='../field/country-names.txt' mode='r' encoding='cp1252'>
# afghanistan : <Response [200]>
# akrotiri : <Response [200]>
# albania : <Response [200]>
# algeria : <Response [200]>
# american-samoa : <Response [200]>
# andorra : <Response [200]>
# angola : <Response [200]>
# anguilla : <Response [200]>
# antarctica : <Response [200]>
# antigua-and-barbuda : <Response [200]>
# argentina : <Response [200]>
# armenia : <Response [200]>
# aruba : <Response [200]>
# ashmore-and-cartier-islands : <Response [200]>
# australia : <Response [200]>
# austria : <Response [200]>
# azerbaijan : <Response [200]>
# bahamas-the : <Response [200]>
# bahrain : <Response [200]>
# baker-island : <Response [200]>
# bangladesh : <Response [200]>
# barbados : <Response [200]>
# belarus : <Response [200]>
# belgium : <Response [200]>
# belize : <Response [200]>
# benin : <Response [200]>
# bermuda : <Response [200]>
# bhutan : <Response [200]>
# bolivia : <Response [200]>
# bosnia-and-herzegovina : <Response [200]>
# botswana : <Response [200]>
# bouvet-island : <Response [200]>
# brazil : <Response [200]>
# british-indian-ocean-territory : <Response [200]>
# british-virgin-islands : <Response [200]>
# brunei : <Response [200]>
# bulgaria : <Response [200]>
# burkina-faso : <Response [200]>
# burma : <Response [200]>
# burundi : <Response [200]>
# cabo-verde : <Response [200]>
# cambodia : <Response [200]>
# cameroon : <Response [200]>
# canada : <Response [200]>
# cayman-islands : <Response [200]>
# central-african-republic : <Response [200]>
# chad : <Response [200]>
# chile : <Response [200]>
# china : <Response [200]>
# christmas-island : <Response [200]>
# clipperton-island : <Response [200]>
# cocos-keeling-islands : <Response [200]>
# colombia : <Response [200]>
# comoros : <Response [200]>
# congo-democratic-republic-of-the : <Response [200]>
# congo-republic-of-the : <Response [200]>
# cook-islands : <Response [200]>
# coral-sea-islands : <Response [200]>
# costa-rica : <Response [200]>
# cote-divoire : <Response [200]>
# croatia : <Response [200]>
# cuba : <Response [200]>
# curacao : <Response [200]>
# cyprus : <Response [200]>
# czechia : <Response [200]>
# denmark : <Response [200]>
# dhekelia : <Response [200]>
# djibouti : <Response [200]>
# dominica : <Response [200]>
# dominican-republic : <Response [200]>
# ecuador : <Response [200]>
# egypt : <Response [200]>
# el-salvador : <Response [200]>
# equatorial-guinea : <Response [200]>
# eritrea : <Response [200]>
# estonia : <Response [200]>
# eswatini : <Response [200]>
# ethiopia : <Response [200]>
# european-union : <Response [200]>
# falkland-islands-islas-malvinas : <Response [200]>
# faroe-islands : <Response [200]>
# fiji : <Response [200]>
# finland : <Response [200]>
# france : <Response [200]>
# french-polynesia : <Response [200]>
# french-southern-and-antarctic-lands : <Response [200]>
# gabon : <Response [200]>
# gambia-the : <Response [200]>
# gaza-strip : <Response [200]>
# georgia : <Response [200]>
# germany : <Response [200]>
# ghana : <Response [200]>
# gibraltar : <Response [200]>
# greece : <Response [200]>
# greenland : <Response [200]>
# grenada : <Response [200]>
# guam : <Response [200]>
# guatemala : <Response [200]>
# guernsey : <Response [200]>
# guinea : <Response [200]>
# guinea-bissau : <Response [200]>
# guyana : <Response [200]>
# haiti : <Response [200]>
# heard-island-and-mcdonald-islands : <Response [200]>
# holy-see-vatican-city : <Response [200]>
# honduras : <Response [200]>
# hong-kong : <Response [200]>
# howland-island : <Response [200]>
# hungary : <Response [200]>
# iceland : <Response [200]>
# india : <Response [200]>
# indonesia : <Response [200]>
# iran : <Response [200]>
# iraq : <Response [200]>
# ireland : <Response [200]>
# isle-of-man : <Response [200]>
# israel : <Response [200]>
# italy : <Response [200]>
# jamaica : <Response [200]>
# jan-mayen : <Response [200]>
# japan : <Response [200]>
# jarvis-island : <Response [200]>
# jersey : <Response [200]>
# johnston-atoll : <Response [200]>
# jordan : <Response [200]>
# kazakhstan : <Response [200]>
# kenya : <Response [200]>
# kingman-reef : <Response [200]>
# kiribati : <Response [200]>
# korea-north : <Response [200]>
# korea-south : <Response [200]>
# kosovo : <Response [200]>
# kuwait : <Response [200]>
# kyrgyzstan : <Response [200]>
# laos : <Response [200]>
# latvia : <Response [200]>
# lebanon : <Response [200]>
# lesotho : <Response [200]>
# liberia : <Response [200]>
# libya : <Response [200]>
# liechtenstein : <Response [200]>
# lithuania : <Response [200]>
# luxembourg : <Response [200]>
# macau : <Response [200]>
# madagascar : <Response [200]>
# malawi : <Response [200]>
# malaysia : <Response [200]>
# maldives : <Response [200]>
# mali : <Response [200]>
# malta : <Response [200]>
# marshall-islands : <Response [200]>
# mauritania : <Response [200]>
# mauritius : <Response [200]>
# mexico : <Response [200]>
# micronesia-federated-states-of : <Response [200]>
# midway-islands : <Response [200]>
# moldova : <Response [200]>
# monaco : <Response [200]>
# mongolia : <Response [200]>
# montenegro : <Response [200]>
# montserrat : <Response [200]>
# morocco : <Response [200]>
# mozambique : <Response [200]>
# namibia : <Response [200]>
# nauru : <Response [200]>
# navassa-island : <Response [200]>
# nepal : <Response [200]>
# netherlands : <Response [200]>
# new-caledonia : <Response [200]>
# new-zealand : <Response [200]>
# nicaragua : <Response [200]>
# niger : <Response [200]>
# nigeria : <Response [200]>
# niue : <Response [200]>
# norfolk-island : <Response [200]>
# north-macedonia : <Response [200]>
# northern-mariana-island : <Response [404]>
# norway : <Response [200]>
# oman : <Response [200]>
# pakistan : <Response [200]>
# palau : <Response [200]>
# palmyra-atoll : <Response [200]>
# panama : <Response [200]>
# papua-new-guinea : <Response [200]>
# paracel-islands : <Response [200]>
# paraguay : <Response [200]>
# peru : <Response [200]>
# philippines : <Response [200]>
# pitcairn-islands : <Response [200]>
# poland : <Response [200]>
# portugal : <Response [200]>
# puerto-rico : <Response [200]>
# qatar : <Response [200]>
# romania : <Response [200]>
# russia : <Response [200]>
# rwanda : <Response [200]>
# saint-barthelemy : <Response [200]>
# saint-helena-ascension-and-tristan-da-cunha : <Response [200]>
# saint-kitts-and-nevis : <Response [200]>
# saint-lucia : <Response [200]>
# saint-martin : <Response [200]>
# saint-pierre-and-miquelon : <Response [200]>
# saint-vincent-and-the-grenadines : <Response [200]>
# samoa : <Response [200]>
# san-marino : <Response [200]>
# sao-tome-and-principe : <Response [200]>
# saudi-arabia : <Response [200]>
# senegal : <Response [200]>
# serbia : <Response [200]>
# seychelles : <Response [200]>
# sierra-leone : <Response [200]>
# singapore : <Response [200]>
# sint-maarten : <Response [200]>
# slovakia : <Response [200]>
# slovenia : <Response [200]>
# solomon-islands : <Response [200]>
# somalia : <Response [200]>
# south-africa : <Response [200]>
# south-georgia-and-south-sandwich-islands : <Response [200]>
# south-sudan : <Response [200]>
# spain : <Response [200]>
# spratly-islands : <Response [200]>
# sri-lanka : <Response [200]>
# sudan : <Response [200]>
# suriname : <Response [200]>
# svalbard : <Response [200]>
# sweden : <Response [200]>
# switzerland : <Response [200]>
# syria : <Response [200]>
# taiwan : <Response [200]>
# tajikistan : <Response [200]>
# tanzania : <Response [200]>
# thailand : <Response [200]>
# timor-leste : <Response [200]>
# togo : <Response [200]>
# tokelau : <Response [200]>
# tonga : <Response [200]>
# trinidad-and-tobago : <Response [200]>
# tunisia : <Response [200]>
# turkey : <Response [200]>
# turkmenistan : <Response [200]>
# turks-and-caicos-islands : <Response [200]>
# tuvalu : <Response [200]>
# uganda : <Response [200]>
# ukraine : <Response [200]>
# united-arab-emirates : <Response [200]>
# united-kingdom : <Response [200]>
# united-states : <Response [200]>
# united-states-pacific-island-wildlife-refuges : <Response [200]>
# uruguay : <Response [200]>
# uzbekistan : <Response [200]>
# vanuatu : <Response [200]>
# venezuela : <Response [200]>
# vietnam : <Response [200]>
# virgin-islands : <Response [200]>
# wake-island : <Response [200]>
# wallis-and-futuna : <Response [200]>
# west-bank : <Response [200]>
# world : <Response [200]>
# yemen : <Response [200]>
# zambia : <Response [200]>
# zimbabwe : <Response [200]>
#
# Process finished with exit code 0
###