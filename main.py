country_cont = input("TYPE THE NAME OF THE COUNTRY/CONTINENT WHOSE LIFE EXPECTANCY YOU WANT TO SEE "
                     "(to see the average global life expectancy, type GLOBAL) HERE: ")

if country_cont.upper() == "GLOBAL":
    import GLOBAL
elif country_cont.upper() == "AFRICA":
    import AFRICA
elif country_cont.upper() == "AUSTRALIA":
    import AUSTRALIA
elif country_cont.upper() == "INDIA":
    import INDIA
elif country_cont.upper() == "EUROPE":
    import EU
elif country_cont.upper() == "NORTH AMERICA":
    import NorthAm
elif country_cont.upper() == "SOUTH AMERICA":
    import SouthAm
elif country_cont.upper() == "ASIA":
    import ASIA
